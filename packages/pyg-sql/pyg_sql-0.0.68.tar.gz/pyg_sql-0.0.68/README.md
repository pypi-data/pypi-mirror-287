# pyg-sql

## Introduction

* pip install from https://pypi.org/project/pyg-sql/
* conda install: I no longer maintain a conda environment so an old version is available here: https://anaconda.org/yoavgit/pyg-sql. The project itself will happily conda-build.

pyg-sql creates sql_cursor (and its constructor, sql_table), a thin wrapper on sql-alchemy (sa.Table), providing three different functionailities:

* simplified create/filter/sort/access/join of a sql table
* creation of a full no-sql like document-store
* full "in-the-background" maintainance of indexed unique records are per specified primary keys while we auto-archive old data
* supports both a transactional and an ad-hoc approach

pyg-sql supports very light joins but makes playing with a single table MUCH easier than traditional sqlalchemy.

## access simplification

sqlalchemy use-pattern makes Table create the "statement" and then let the engine session/connection execute. Conversely, the sql_cursor keeps tabs internally of:

    - the table
    - the engine
    - the "select", the "order by" and the "where" expressions

This allows us to
    - "query and execute" in one go
    - build statements interactively, each time adding select/where/sort to previous where/select
    

    :Example: table creation
    ------------------------
    >>> from pyg_base import * 
    >>> from pyg_sql import * 
    >>> import datetime
    
    >>> t = sql_table(db = 'test_db', table = 'students', non_null = ['name', 'surname'], server = 'DESKTOP-LU5C5QF',
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float))
    >>> t = t.delete()


    :Example: table insertion
    -------------------------
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> t = t.insert(name = 'anna', surname = 'git', age = 37)
    >>> assert len(t) == 2
    >>> t = t.insert(name = ['ayala', 'itamar', 'opher'], surname = 'gate', age = [17, 11, 16])
    >>> assert len(t) == 5

    :Example: simple access
    -----------------------
    You can access rows either as dicts or as pd.Series
    
    >>> t[0]
    
    {'_id': 1,
     'created': datetime.datetime(2023, 1, 23, 17, 0, 6, 553000),
     'name': 'yoav',
     'surname': 'git',
     'doc': None,
     'details': None,
     'dob': None,
     'age': 48,
     'grade': None}

    >>> t.df[0]
    _id                                 1
    created    2023-01-23 17:00:06.553000
    name                             yoav
    surname                           git
    doc                              None
    details                          None
    dob                              None
    age                                48
    grade                            None
    dtype: object
    
    >>> assert t.sort('age')[0].name == 'itamar'                                                     # youngest
    >>> assert t.sort('age')[-1].name == 'yoav'                                                      # access of last record
    >>> assert t.sort(dict(age=-1))[0].name == 'yoav'                                                # sort in descending order
    >>> assert t.sort('name')[::].name == ['anna', 'ayala', 'itamar', 'opher', 'yoav']
    >>> assert t.sort('name')[['name', 'surname']][::].shape == (5, 2)                              ## access of specific column(s)
    >>> assert t.surname == ['gate', 'git']
    >>> assert t['surname'] == ['gate', 'git']
    >>> assert t[dict(name = 'yoav')] == t.inc(name = 'yoav')[0]

    >>> names = [doc.name for doc in t.sort(dict(age=-1))]
    >>> assert names == ['yoav', 'anna', 'ayala', 'opher', 'itamar']

    :Example: DataFrame access:
    ---------------------------
    >>> t.df() ## get all the data as a dataframe
    >>> t.sort('age')[['age', 'name']].df[2:4]

       age   name
    0   17  ayala
    1   37   anna    

    :Example: simple filtering
    --------------------------
    >>> assert len(t.inc(surname = 'gate')) == 3
    >>> assert len(t.inc(surname = 'gate').inc(name = 'ayala')) == 1    # you can build filter in stages
    >>> assert len(t.inc(surname = 'gate', name = 'ayala')) == 1        # or build in one step
    >>> assert len(t.inc(surname = 'gate').exc(name = 'ayala')) == 2

    >>> assert len(t > dict(age = 30)) == 2
    >>> assert len(t <= dict(age = 37)) == 4
    >>> assert len(t.inc(t.c.age > 30)) == 2  # can filter using the standard sql-alchemy .c.column objects
    >>> assert len(t.where(t.c.age > 30)) == 2  # can filter using the standard sql-alchemy "where" statement 

## insertion of "documents" into string columns...

It is important to realise that we already have much flexibility behind the scene in using "documents" inside string columns:

    >>> t = t.delete()
    >>> assert len(t) == 0; assert t.count() == 0
    >>> import numpy as np
    >>> t.insert(name = 'yoav', surname = 'git', details = dict(kids = {'ayala' : dict(age = 17, gender = 'f'), 'opher' : dict(age = 16, gender = 'f'), 'itamar': dict(age = 11, gender = 'm')}, salary = np.array([100,200,300]), ))

    >>> t[0] # we can grab the full data back!

    {'_id': 81,
     'created': datetime.datetime(2022, 6, 30, 0, 10, 33, 900000),
     'name': 'yoav',
     'surname': 'git',
     'doc': None,
     'details': {'kids': {'ayala':  {'age': 17, 'gender': 'f'},
                          'opher':  {'age': 16, 'gender': 'f'},
                          'itamar': {'age': 11, 'gender': 'm'}},
                 'salary': array([100, 200, 300])},
     'dob': None,
     'age': None,
     'grade': None}

    >>> class Temp():
            pass
            
    >>> t.insert(name = 'anna', surname = 'git', details = dict(temp = Temp())) ## yep, we can store actual objects...
    >>> t[1]  # and get them back as proper objects on loading

    {'_id': 83,
     'created': datetime.datetime(2022, 6, 30, 0, 16, 10, 340000),
     'name': 'anna',
     'surname': 'git',
     'doc': None,
     'details': {'temp': <__main__.Temp at 0x1a91d9fd3a0>},
     'dob': None,
     'age': None,
     'grade': None}

## primary keys and auto-archive

Primary Keys are applied if the primary keys (pk) are specified. 
Now, when we insert into a table, if another record with same pk exists, the record will be replaced.
Rather than simply delete old records, we create automatically a parallel database.archived_schema.table to auto-archive these replaced records.
This ensure a full audit and roll-back of records is possible.

    :Example: primary keys and deleted records
    ------------------------------------------
    The table as set up can have multiple items so:
    
    >>> from pyg import * 
    >>> t = t.delete()
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 46)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 47)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> assert len(t) == 3
    
    >>> t = t.delete() 
    >>> t = sql_table(db = 'test', table = 'students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'])         ## <<<------- We set primary keys

    >>> t = t.delete()
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 46)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 47)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> assert len(t) == 1 
    >>> assert t[0].age == 48

    Where did the data go to? We automatically archive the deleted old records for dict(name = 'yoav', surname = 'git') here:

    >>> t.archived()
    
    t.archived() is a table by same name,
    
    - exists on same database, schema name changed prefixed with 'archived_'
    - same table structure with added 'deleted' column into the primary keys
    
    >>> assert len(t.archived().inc(name = 'yoav', age = 46)) > 0
    >>> t.archived().delete() 

## sql_cursor as a document store

    If we set doc = True, the table will be viewed internally as a no-sql-like document store. 

    - the nullable columns supplied are the columns on which querying will be possible
    - the primary keys are still used to ensure we have one document per unique pk
    - the document is jsonified (handling non-json stuff like dates, np.array and pd.DataFrames) and put into the 'doc' column in the table, but this is invisible to the user.

    :Example: doc management
    ------------------------
    
    We now suppose that we are not sure what records we want to keep for each student

    >>> from pyg import *
    >>> import datetime
    >>> t = sql_table(db = 'test', table = 'unstructured_students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'],
                          doc = True)   ##<---- The table will actually be a document store

    We are now able to keep varied structure per each record. 

    >>> t = t.delete()
    
    >>> doc = dict(name = 'yoav', surname = 'git', age = 30, profession = 'coder', children = ['ayala', 'opher', 'itamar'])
    >>> inserted_doc = t.insert_one(doc)
    >>> assert t.inc(name = 'yoav', surname = 'git')[0].children == ['ayala', 'opher', 'itamar']

    >>> doc2 = dict(name = 'anna', surname = 'git', age = 28, employer = 'Cambridge University', hobbies = ['chess', 'music', 'swimming'])
    >>> _ = t.insert_one(doc2)
    >>> assert t[dict(age = 28)].hobbies == ['chess', 'music', 'swimming']  # Note that we can filter or search easily using the column 'age' that was specified in table. We cannot do this on 'employer'
    
    :Example: document store containing pd.DataFrames.
    ----------
    
    >>> from pyg import *
    >>> doc = dict(name = 'yoav', surname = 'git', age = 35, 
                   salary = pd.Series([100,200,300], drange(2)),
                   costs = dict(fixed_cost     = 100, 
                                variable_costs = pd.DataFrame(dict(transport = [0,1,2], food = [4,5,6], education = [10,20,30]), drange(2))))  # pandas object is in doc.costs.variable_costs
    
    >>> t = sql_table(db = 'test', table = 'unstructured_students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'],
                          writer = 'c:/temp/%name/%surname.parquet', ##<---- The location where pd.DataFrame/Series are to be stored
                          doc = True)   

    >>> inserted = t.insert_one(doc)
    >>> import os
    >>> assert 'salary.parquet' in os.listdir('c:/temp/yoav/git')
    >>> assert 'variable_costs.parquet' in os.listdir('c:/temp/yoav/git/costs') ## yes, dicts of dicts, or dicts of lists are all fine...
    
    We can now access the data seemlessly:

    >>> read_from_db = t.inc(name = 'yoav')[0]     
    >>> read_from_file = pd_read_parquet('c:/temp/yoav/git/salary.parquet')
    >>> assert list(read_from_db.salary.values) == [100, 200, 300]
    >>> assert list(read_from_file.values) == [100, 200, 300]
    
