# OportunityReportCadMusRPA

> Status: ready to homolog ⚠️

### This RPA Solution must open the CadMus Page, get all oportunities enable and genarate an Excel File and send to the area analyze

## STEP-1 OPEN_PAGE
+ When we open the page we need only  WAIT for the elements appear
+ then the rest of the code happen in background. Once we open the page and
+ all the elements exists (oportunities,locale,Detail), the application saves it  in LOCALSTORAGE

## STEP-2 GET_OPORTUNITIES
+ Using Python libs path Libs/LocalStorage.py we are able to get 
+ all OPORTUNITIES and manipulate it using Json Lib and return as DATA

## STEP-3 EXPORT_TO_EXCEL
+ Using Python lib Pandas we are able to get all Data(Json) returned and
+ and generate a DataFrame(Pandas) to convert into a Excel File.

## STEP-4 SEND_EMAIL_TO_AREA
+ Using a script lib path Libs/SednEmail.py we  are able to send e-mail
+ to the are with the excel generate
  #### This step require a SMTP e-mail credentials on line 75 file path  "Libs/SendEmail.py" ⚠️






### Technologies Used:
<table>
  <tr>
  <td>Python</td>
  <td> ChromeDriver</td>
  </tr>
  <td>3.10.0</td>
  <td>97.0.4692.71</td>
  <tr>
  </tr> 
</table>

## How to run the application:
#### Install: Python
#### Run Shell: Pip Install -r requirements.txt
