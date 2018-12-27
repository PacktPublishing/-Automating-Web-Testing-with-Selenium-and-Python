# Creating a testing suite 

Example web app: https://opensource-demo.orangehrmlive.com

## TC (Test Case) definitions 

### Login TCs

Username : Admin | Password : admin123

| TCID | TC Name | Description | 
| --- | --- | --- | 
| [TC_L_001](#TC_L_001) | Login page loaded | Checking if the key elements on the page are loaded. Login fields and login button. | 
| [TC_L_002](#TC_L_002) | Successful login | Using correct username and pass and verifying succseful login. |  
| [TC_L_003](#TC_L_003) | Failed login | Using incorrect password and verifying the error message for failed login. |  

---


| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_001 <a name="TC_L_001"></a> | Login page loaded | Checking if the key elements on the page are loaded. Login fields and login button. |  

```yaml
Preconditions:
  - None
Steps:
  1. Verify Login panel exists 
  2. Verify Username input filed exists 
  3. Verify Password field exists 
  4. Verify Login button exists and enabled for clicking 
Expected results: >
    All test steps passed as excepted. 
```

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_002 <a name="TC_L_002"></a> | Successful login | Using correct username and pass and verifying succseful login. |  

```yaml
Preconditions:
  - None
Steps:
  1. Enter user name Admin in the username field
  2. Enter passerod admin123 in password field 
  3. Click on the Login button 
  4. Verify correct redirection to Dashboard - correct url 
  5. Verify that Dashboard is loaded 
Expected results: >
    Login successful and after login, redirected to Dashboard page. 
```

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_003 <a name="TC_L_003"></a> | Failed login | Using incorrect password and verifying the error message for failed login. |  

```yaml
Preconditions:
  - None
Steps:
  1. Enter user name Admin in the username field
  2. Enter passerod password in password field 
  3. Verify the correct message is displayed  
Expected results: >
    All test steps passed as excepted. 
```

---


