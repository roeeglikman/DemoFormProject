
##-----Imports-----##
##--imports all the ibraries for the forms---##from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField, SelectMultipleField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
### ----------------------------------------------------------- ###







## This class have the fields that are part of the Login form.
##   This form will get from the user a 'username' and a 'password' and sent to the server
##   to check if this user is authorised to continue
## You can see three fields:
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



## This class have the fields of a registration form
##   This form is where the user can register himself. It will have sll the information
##   we want to save on a user (general information) and the username ans PW the new user want to have
## You can see three fields:
##   the 'FirstName' field - will be used to get the first name of the user
##   the 'LastName' field - will be used to get the last name of the user
##   the 'PhoneNum' field - will be used to get the phone number of the user
##   the 'EmailAddr' field - will be used to get the E-Mail of the user
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')

## This class have the fields that the user can set, to have the query parameters for analysing the data
##   This form is where the user can set different parameters, depand on your project,
##   that will be used to do the data analysis (using Pandas etc.)
## You can see three fields:
##   The fields that will be part of this form are specific to your project
##   Please complete this class according to your needs
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
#class DataParametersFormStructure(FlaskForm):
#    
#    submit = SubmitField('Submit')


##------------Expand buttom---------##
## builts the buttom that allows the user to open the table of the dataset 
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"
    ### ----------------------------------------------------------- ###


    ##------------Collapse buttom---------##
## builts the buttom that allows the user to close the table of the dataset
class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"
    ### ----------------------------------------------------------- ###

    ##----------------------------QueryFormStructure------------------------##
## This class have the fields that are part of the nba-salary demonstration
## You can see two fields:
##   the 'teams' field - will be used to get the teams in order to make a graph that presents injuries for the teams that the user chose.
##   the 'year' field - the user will see a graph that present the injurie in the year and the teams that he choes.
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class QueryForm(FlaskForm):
    teams  = SelectMultipleField('Select teams:  ' , validators = [DataRequired()])
    year   = StringField('Enter the year:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')
    ### ----------------------------------------------------------- ###