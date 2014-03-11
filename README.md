# Django Excercises

## Instructions

this goes in a `django_excercises` folder under `/vagrant/python-test`

    mkdir /vagrant/python-test/django_excercises
    cd /vagrant/python-test/django_excercises
    touch school_client.py
    # ... and so on ....


## Features

Implement a django server and a python command line client to manage a school's enrolment system.

Components:

 - django project named `school_pro`
 - django app named `enrolment`
 - python command line client named `school_client.py`

The enrolment app exposes a web service for the command line client to enroll students saving their details in a db.


### Store student

The school staff uses the command line client to add a student to the database.

    $ python school_client.py enroll --f_name John --l_name Doe
    OK

    --f_name rappresent the first name of student
    --l_name rappresent the last name of student

The command line client prints `OK` if the operation went correctly.

The clerk can add more students:

    $ python school_client.py enroll --f_name John --l_name Doe
    OK
    $ python school_client.py enroll --f_name John --l_name Doe
    OK
    $ python school_client.py enroll --f_name John --l_name Doe
    OK


### Search students

The school staff uses the command line client to list all the enrolled students

    $ python school_client.py search --student Jane
    OK listing results:
    Jane Austen
    Jane Austen
    Jane Austen


The client first displays an informative line and then prints out all the matching students one per line.

Bonus: search on both first name and last name.

THE CLIENT SEARCH ON BOTH FIRST AND LAST NAME

### Persist enrollment date and time  (optional)

The system saves date and time of enrolment when the staff enrols a student.

The enrolment date and time is displayed in the search results.


    $ python school_client.py search Jane
    OK listing results:
    Jane Austen 2014-01-01T12:00:00
    Jane Austen 2014-01-01T12:00:00
    Jane Austen 2014-01-01T12:00:00


*HINT 1* use DateTimeField for models

*HINT 2* datetime is not natively json-encodable, turn it into a string before
encoding it


# Submission

Push all the excercises to your github repo and make `mpaolini` a contributor:

 - login into github and create a new repo named `ial-python-test`
 - go to repo settings (bottom right), then collaborators (left column), write `mpaolini` and click "Add collaborator"
 - `git init`
 - `git add .`
 - `git commit -m test finished`
 - `git remote add origin https://github.com/<username>/ial-python-test.git` 
 - `git push -u origin master`
