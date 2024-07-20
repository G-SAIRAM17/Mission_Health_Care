from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import patientSignUp,doctorSignUp,receptionistSignUp,labtechnicianSignUp,adminSignUp,timeSlot
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import random
import string
import datetime

#-----------------------Patient Signup View-------------------------------------------------------------
def psignup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if patientSignUp.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('psignup')
            else:
                patientSignUp.objects.create(name=name, age=age, gender=gender, email=email, mobile=mobile, address=address, password=password,profile_pic=null)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
                <title> Welcome to Integrated Health Care Portal </title>
                <!--[if !mso]><!-- -->
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <!--<![endif]-->
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <style type="text/css">
                  #outlook a {{
                    padding: 0;
                  }}

                  body {{
                    margin: 0;
                    padding: 0;
                    -webkit-text-size-adjust: 100%;
                    -ms-text-size-adjust: 100%;
                  }}

                  table,
                  td {{
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                  }}

                  img {{
                    border: 0;
                    height: auto;
                    line-height: 100%;
                    outline: none;
                    text-decoration: none;
                    -ms-interpolation-mode: bicubic;
                  }}

                  p {{display: block;
                    margin: 13px 0;
                  }}
                </style>
                <!--[if mso]>
                      <xml>
                      <o:OfficeDocumentSettings>
                        <o:AllowPNG/>
                        <o:PixelsPerInch>96</o:PixelsPerInch>
                      </o:OfficeDocumentSettings>
                      </xml>
                      <![endif]-->
                <!--[if lte mso 11]>
                      <style type="text/css">
                        .mj-outlook-group-fix {{width:100% !important;}}
                      </style>
                      <![endif]-->
                <style type="text/css">
                  @media only screen and (min-width:480px) {{
                    .mj-column-per-100 {{
                      width: 100% !important;
                      max-width: 100%;
                    }}
                  }}
                </style>
                <style type="text/css">
                  @media only screen and (max-width:480px) {{
                    table.mj-full-width-mobile {{
                      width: 100% !important;
                    }}

                    td.mj-full-width-mobile {{
                      width: auto !important;
                    }}
                  }}
                </style>
                <style type="text/css">
                  a,
                  span,
                  td,
                  th {{
                    -webkit-font-smoothing: antialiased !important;
                    -moz-osx-font-smoothing: grayscale !important;
                  }}
                </style>
              </head>

              <body style="background-color:#ffffff;">
                <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">Welcome {name} </div>
                <div style="background-color:#ffffff;">
                  <!--[if mso | IE]>
                    <table
                      align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
                    >
                      <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                      <tbody>
                        <tr>
                          <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                              
                      <tr>
                    
                          <td
                            class="" style="vertical-align:top;width:600px;"
                          >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tbody><tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                      <tbody>
                                        <tr>
                                          <td style="width:50px;">
                                            <img alt="image description" height="auto" src="https://codedmails.com/images/logo-circle.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;" width="50" />
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                                      <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome {name} ! </h1>
                                    </div>
                                  </td>
                                </tr>
                              </tbody></table>
                            </div>
                            <!--[if mso | IE]>
                          </td>
                        
                      </tr>
                    
                                </table>
                              <![endif]-->
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <!--[if mso | IE]>
                        </td>
                      </tr>
                    </table>
                    
                    <table
                      align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
                    >
                      <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                      <tbody>
                        <tr>
                          <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                              
                      <tr>
                    
                          <td
                            class="" style="vertical-align:top;width:600px;"
                          >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tbody><tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">We have approved your request and we are really excited to welcome you.</div>
                                  </td>
                                </tr>
                                <tr>
                                </tr>
                                <tr>
                                  <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                                      <tbody><tr>
                                        <td align="center" bgcolor="#2e58ff" role="presentation" style="border:none;border-radius:30px;cursor:auto;mso-padding-alt:10px 25px;background:#2e58ff;" valign="middle">
                                          <a href="#" style="display: inline-block; background: #2e58ff; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; line-height: 30px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 30px;" target="_blank"> Registration is Completed!!! </a>
                                        </td>
                                      </tr>
                                    </tbody></table>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">If you need any help, don’t hesitate to reach out to us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;">missionintegratedhealthcare@gmail.com</a>!</div>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Regards,</div>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Team Integrated HealthCare</div>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <!--[if mso | IE]>
                    <table
                      align="left" border="0" cellpadding="0" cellspacing="0" role="presentation"
                    >
                      <tr>
                    
                            <td>
                          <![endif]-->
                                    <!--[if mso | IE]>
                            </td>
                          
                            <td>
                          <![endif]-->
                                    <!--[if mso | IE]>
                            </td>
                          
                            <td>
                          <![endif]-->

                                    <!--[if mso | IE]>
                            </td>
                          
                        </tr>
                      </table>
                    <![endif]-->
                                  </td>
                                </tr>
                              </tbody></table>
                            </div>
                            <!--[if mso | IE]>
                          </td>
                        
                      </tr>
                    
                                </table>
                              <![endif]-->
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <!--[if mso | IE]>
                        </td>
                      </tr>
                    </table>
                    
                    <table
                      align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
                    >
                      <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                      <tbody>
                        <tr>
                          <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                              
                      <tr>
                    
                          <td
                            class="" style="vertical-align:top;width:600px;"
                          >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tbody><tr>
                                  <td style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <p style="border-top: dashed 1px lightgrey; font-size: 1px; margin: 0px auto; width: 100%;">
                                    </p>
                                    <!--[if mso | IE]>
                      <table
                        align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:dashed 1px lightgrey;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px"
                      >
                        <tr>
                          <td style="height:0;line-height:0;">
                            &nbsp;
                          </td>
                        </tr>
                      </table>
                    <![endif]-->
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Have questions or need help? Email us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;"> missionintegratedhealthcare@gmail.com</a></div>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Sri Vasavi Engineering College  <br> Tadepalligudem<br /> © 2024 [Mission Integrated Health care] Inc.</div>
                                  </td>
                                </tr>
                                <tr>
                                  <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Update your <a href="#" style="color: #2e58ff; text-decoration: none;">email preferences</a> to choose the types of emails you receive, or you can <a href="#" style="color: #2e58ff; text-decoration: none;"> unsubscribe </a>from all future emails.</div>
                                  </td>
                                </tr>
                              </tbody></table>
                            </div>
                            <!--[if mso | IE]>
                          </td>
                        
                      </tr>
                    
                                </table>
                              <![endif]-->
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <!--[if mso | IE]>
                        </td>
                      </tr>
                    </table>
                    
                    <table
                      align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
                    >
                      <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                      <tbody>
                        <tr>
                          <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                              
                      <tr>
                    
                          <td
                            class="" style="vertical-align:top;width:600px;"
                          >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                              <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tbody><tr>
                                  <td style="font-size:0px;word-break:break-word;">
                                    <!--[if mso | IE]>
                  
                      <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="1" style="vertical-align:top;height:1px;">
                    
                  <![endif]-->
                                    <div style="height:1px;">   </div>
                                    <!--[if mso | IE]>
                  
                      </td></tr></table>
                    
                  <![endif]-->
                                  </td>
                                </tr>
                              </tbody></table>
                            </div>
                            <!--[if mso | IE]>
                          </td>
                        
                      </tr>
                    
                                </table>
                              <![endif]-->
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <!--[if mso | IE]>
                        </td>
                      </tr>
                    </table>
                    <![endif]-->
                </div>
              </body>
              </html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('psuccess')
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('psignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('psignup')
    else:
        return render(request, 'patient/patient_signup.html')

#--------------------------------Doctor Signup View-----------------------------------------
def dsignup(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        specialist=request.POST.get('specialist')
        hname=request.POST.get('hname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if doctorSignUp.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('dsignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('dsignup')
            else:
                doctorSignUp.objects.create(name=name, specialist=specialist,hname=hname, gender=gender, email=email, mobile=mobile, password=password)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi DR. {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
  <title> Welcome to Integrated Health care Portal </title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style type="text/css">
    #outlook a {{
      padding: 0;
    }}

    body {{
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }}

    table,
    td {{
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }}

    img {{
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }}

    p {{display: block;
      margin: 13px 0;
    }}
  </style>
  <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix {{width:100% !important;}}
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {{
      .mj-column-per-100 {{
        width: 100% !important;
        max-width: 100%;
      }}
    }}
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {{
      table.mj-full-width-mobile {{
        width: 100% !important;
      }}

      td.mj-full-width-mobile {{
        width: auto !important;
      }}
    }}
  </style>
  <style type="text/css">
    a,
    span,
    td,
    th {{
      -webkit-font-smoothing: antialiased !important;
      -moz-osx-font-smoothing: grayscale !important;
    }}
  </style>
</head>

<body style="background-color:#ffffff;">
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Preview - Welcome Dr. {name} </div>
  <div style="background-color:#ffffff;">
    <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:50px;">
                              <img alt="image description" height="auto" src="https://codedmails.com/images/logo-circle.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;" width="50" />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                        <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome DR. {name} ! </h1>
                      </div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">We have approved your request and we are really excited to welcome you.</div>
                    </td>
                  </tr>
                  <tr>
                  </tr>
                  <tr>
                    <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                        <tbody><tr>
                          <td align="center" bgcolor="#2e58ff" role="presentation" style="border:none;border-radius:30px;cursor:auto;mso-padding-alt:10px 25px;background:#2e58ff;" valign="middle">
                            <a href="#" style="display: inline-block; background: #2e58ff; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; line-height: 30px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 30px;" target="_blank"> Registration is Completed!!! </a>
                          </td>
                        </tr>
                      </tbody></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">If you need any help, don’t hesitate to reach out to us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;">missionintegratedhealthcare@gmail.com</a>!</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Regards,</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Team Integrated HealthCare</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <!--[if mso | IE]>
      <table
         align="left" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
      
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->

                      <!--[if mso | IE]>
              </td>
            
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <p style="border-top: dashed 1px lightgrey; font-size: 1px; margin: 0px auto; width: 100%;">
                      </p>
                      <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:dashed 1px lightgrey;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Have questions or need help? Email us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;"> missionintegratedhealthcare@gmail.com</a></div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Sri Vasavi Engineering College  <br> Tadepalligudem<br /> © 2024 [Mission Integrated Health care] Inc.</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Update your <a href="#" style="color: #2e58ff; text-decoration: none;">email preferences</a> to choose the types of emails you receive, or you can <a href="#" style="color: #2e58ff; text-decoration: none;"> unsubscribe </a>from all future emails.</div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;word-break:break-word;">
                      <!--[if mso | IE]>
    
        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="1" style="vertical-align:top;height:1px;">
      
    <![endif]-->
                      <div style="height:1px;">   </div>
                      <!--[if mso | IE]>
    
        </td></tr></table>
      
    <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
  </div>
</body>
</html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('dsuccess') 
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('dsignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('dsignup')
  else:
    return render(request,'doctor/doctor_signup.html')

#--------------------------------Receptionist Signup View-----------------------------------------
def rsignup(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        hname=request.POST.get('hname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address=request.POST.get('address')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if receptionistSignUp.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('dsignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('dsignup')
            else:
                receptionistSignUp.objects.create(name=name,hname=hname, gender=gender, email=email, mobile=mobile, address=address,password=password)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi DR. {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
  <title> Welcome to Integrated Health care Portal </title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style type="text/css">
    #outlook a {{
      padding: 0;
    }}

    body {{
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }}

    table,
    td {{
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }}

    img {{
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }}

    p {{display: block;
      margin: 13px 0;
    }}
  </style>
  <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix {{width:100% !important;}}
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {{
      .mj-column-per-100 {{
        width: 100% !important;
        max-width: 100%;
      }}
    }}
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {{
      table.mj-full-width-mobile {{
        width: 100% !important;
      }}

      td.mj-full-width-mobile {{
        width: auto !important;
      }}
    }}
  </style>
  <style type="text/css">
    a,
    span,
    td,
    th {{
      -webkit-font-smoothing: antialiased !important;
      -moz-osx-font-smoothing: grayscale !important;
    }}
  </style>
</head>

<body style="background-color:#ffffff;">
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Preview - Welcome Dr. {name} </div>
  <div style="background-color:#ffffff;">
    <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:50px;">
                              <img alt="image description" height="auto" src="https://codedmails.com/images/logo-circle.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;" width="50" />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                        <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome DR. {name} ! </h1>
                      </div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">We have approved your request and we are really excited to welcome you.</div>
                    </td>
                  </tr>
                  <tr>
                  </tr>
                  <tr>
                    <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                        <tbody><tr>
                          <td align="center" bgcolor="#2e58ff" role="presentation" style="border:none;border-radius:30px;cursor:auto;mso-padding-alt:10px 25px;background:#2e58ff;" valign="middle">
                            <a href="#" style="display: inline-block; background: #2e58ff; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; line-height: 30px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 30px;" target="_blank"> Registration is Completed!!! </a>
                          </td>
                        </tr>
                      </tbody></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">If you need any help, don’t hesitate to reach out to us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;">missionintegratedhealthcare@gmail.com</a>!</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Regards,</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Team Integrated HealthCare</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <!--[if mso | IE]>
      <table
         align="left" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
      
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->

                      <!--[if mso | IE]>
              </td>
            
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <p style="border-top: dashed 1px lightgrey; font-size: 1px; margin: 0px auto; width: 100%;">
                      </p>
                      <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:dashed 1px lightgrey;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Have questions or need help? Email us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;"> missionintegratedhealthcare@gmail.com</a></div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Sri Vasavi Engineering College  <br> Tadepalligudem<br /> © 2024 [Mission Integrated Health care] Inc.</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Update your <a href="#" style="color: #2e58ff; text-decoration: none;">email preferences</a> to choose the types of emails you receive, or you can <a href="#" style="color: #2e58ff; text-decoration: none;"> unsubscribe </a>from all future emails.</div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;word-break:break-word;">
                      <!--[if mso | IE]>
    
        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="1" style="vertical-align:top;height:1px;">
      
    <![endif]-->
                      <div style="height:1px;">   </div>
                      <!--[if mso | IE]>
    
        </td></tr></table>
      
    <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
  </div>
</body>
</html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('rsuccess') 
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('rsignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('rsignup')
  else:
    return render(request,'receptionist/receptionist_signup.html')

#--------------------------------Lab Technician Signup View-----------------------------------------
def lsignup(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        lname=request.POST.get('lname')
        laddress=request.POST.get('laddress')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if labtechnicianSignUp.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('lsignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('lsignup')
            else:
                labtechnicianSignUp.objects.create(name=name, gender=gender, email=email, mobile=mobile,lname=lname, laddress=laddress,password=password)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi DR. {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
  <title> Welcome to Integrated Health care Portal </title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style type="text/css">
    #outlook a {{
      padding: 0;
    }}

    body {{
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }}

    table,
    td {{
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }}

    img {{
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }}

    p {{display: block;
      margin: 13px 0;
    }}
  </style>
  <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix {{width:100% !important;}}
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {{
      .mj-column-per-100 {{
        width: 100% !important;
        max-width: 100%;
      }}
    }}
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {{
      table.mj-full-width-mobile {{
        width: 100% !important;
      }}

      td.mj-full-width-mobile {{
        width: auto !important;
      }}
    }}
  </style>
  <style type="text/css">
    a,
    span,
    td,
    th {{
      -webkit-font-smoothing: antialiased !important;
      -moz-osx-font-smoothing: grayscale !important;
    }}
  </style>
</head>

<body style="background-color:#ffffff;">
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Preview - Welcome Dr. {name} </div>
  <div style="background-color:#ffffff;">
    <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:50px;">
                              <img alt="image description" height="auto" src="https://codedmails.com/images/logo-circle.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;" width="50" />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                        <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome DR. {name} ! </h1>
                      </div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">We have approved your request and we are really excited to welcome you.</div>
                    </td>
                  </tr>
                  <tr>
                  </tr>
                  <tr>
                    <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                        <tbody><tr>
                          <td align="center" bgcolor="#2e58ff" role="presentation" style="border:none;border-radius:30px;cursor:auto;mso-padding-alt:10px 25px;background:#2e58ff;" valign="middle">
                            <a href="#" style="display: inline-block; background: #2e58ff; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; line-height: 30px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 30px;" target="_blank"> Registration is Completed!!! </a>
                          </td>
                        </tr>
                      </tbody></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">If you need any help, don’t hesitate to reach out to us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;">missionintegratedhealthcare@gmail.com</a>!</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Regards,</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Team Integrated HealthCare</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <!--[if mso | IE]>
      <table
         align="left" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
      
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->

                      <!--[if mso | IE]>
              </td>
            
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <p style="border-top: dashed 1px lightgrey; font-size: 1px; margin: 0px auto; width: 100%;">
                      </p>
                      <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:dashed 1px lightgrey;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Have questions or need help? Email us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;"> missionintegratedhealthcare@gmail.com</a></div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Sri Vasavi Engineering College  <br> Tadepalligudem<br /> © 2024 [Mission Integrated Health care] Inc.</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Update your <a href="#" style="color: #2e58ff; text-decoration: none;">email preferences</a> to choose the types of emails you receive, or you can <a href="#" style="color: #2e58ff; text-decoration: none;"> unsubscribe </a>from all future emails.</div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;word-break:break-word;">
                      <!--[if mso | IE]>
    
        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="1" style="vertical-align:top;height:1px;">
      
    <![endif]-->
                      <div style="height:1px;">   </div>
                      <!--[if mso | IE]>
    
        </td></tr></table>
      
    <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
  </div>
</body>
</html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('lsuccess') 
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('lsignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('lsignup')
  else:
    return render(request,'lab_technician/lab_technician_signup.html')

#--------------------------------Admin Signup View-----------------------------------------
def asignup(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        designation=request.POST.get('designation')
        hname=request.POST.get('hname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if adminSignUp.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('asignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('asignup')
            else:
                adminSignUp.objects.create(name=name, designation=designation,hname=hname , mobile=mobile, email=email,password=password)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi DR. {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
  <title> Welcome to Integrated Health care Portal </title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style type="text/css">
    #outlook a {{
      padding: 0;
    }}

    body {{
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }}

    table,
    td {{
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }}

    img {{
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }}

    p {{display: block;
      margin: 13px 0;
    }}
  </style>
  <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix {{width:100% !important;}}
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {{
      .mj-column-per-100 {{
        width: 100% !important;
        max-width: 100%;
      }}
    }}
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {{
      table.mj-full-width-mobile {{
        width: 100% !important;
      }}

      td.mj-full-width-mobile {{
        width: auto !important;
      }}
    }}
  </style>
  <style type="text/css">
    a,
    span,
    td,
    th {{
      -webkit-font-smoothing: antialiased !important;
      -moz-osx-font-smoothing: grayscale !important;
    }}
  </style>
</head>

<body style="background-color:#ffffff;">
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Preview - Welcome Dr. {name} </div>
  <div style="background-color:#ffffff;">
    <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:50px;">
                              <img alt="image description" height="auto" src="https://codedmails.com/images/logo-circle.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;" width="50" />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                        <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome DR. {name} ! </h1>
                      </div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">We have approved your request and we are really excited to welcome you.</div>
                    </td>
                  </tr>
                  <tr>
                  </tr>
                  <tr>
                    <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                        <tbody><tr>
                          <td align="center" bgcolor="#2e58ff" role="presentation" style="border:none;border-radius:30px;cursor:auto;mso-padding-alt:10px 25px;background:#2e58ff;" valign="middle">
                            <a href="#" style="display: inline-block; background: #2e58ff; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; line-height: 30px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 30px;" target="_blank"> Registration is Completed!!! </a>
                          </td>
                        </tr>
                      </tbody></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">If you need any help, don’t hesitate to reach out to us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;">missionintegratedhealthcare@gmail.com</a>!</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Regards,</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#434245;">Team Integrated HealthCare</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <!--[if mso | IE]>
      <table
         align="left" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
      
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->
                      <!--[if mso | IE]>
              </td>
            
              <td>
            <![endif]-->

                      <!--[if mso | IE]>
              </td>
            
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <p style="border-top: dashed 1px lightgrey; font-size: 1px; margin: 0px auto; width: 100%;">
                      </p>
                      <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:dashed 1px lightgrey;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Have questions or need help? Email us at <a href="mailto:missionintegratedhealthcare@gmail.com" style="color: #2e58ff; text-decoration: none;"> missionintegratedhealthcare@gmail.com</a></div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Sri Vasavi Engineering College  <br> Tadepalligudem<br /> © 2024 [Mission Integrated Health care] Inc.</div>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <div style="font-family:Helvetica, Arial, sans-serif;font-size:14px;font-weight:400;line-height:24px;text-align:left;color:#999999;">Update your <a href="#" style="color: #2e58ff; text-decoration: none;">email preferences</a> to choose the types of emails you receive, or you can <a href="#" style="color: #2e58ff; text-decoration: none;"> unsubscribe </a>from all future emails.</div>
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
    <div style="margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
              <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                  <tbody><tr>
                    <td style="font-size:0px;word-break:break-word;">
                      <!--[if mso | IE]>
    
        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="1" style="vertical-align:top;height:1px;">
      
    <![endif]-->
                      <div style="height:1px;">   </div>
                      <!--[if mso | IE]>
    
        </td></tr></table>
      
    <![endif]-->
                    </td>
                  </tr>
                </tbody></table>
              </div>
              <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
  </div>
</body>
</html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('asuccess')
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('asignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('asignup')
  else:
    return render(request,'admin/admin_signup.html')


#---------------Patient Login View-----------------------------------------
def plogin(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            # Retrieve patient based on mobile
            patient = patientSignUp.objects.get(mobile=mobile)

            if patient.password == password:
                # Password matches, log in user
                # Here, you might want to consider using Django's built-in authentication system
                return redirect('pdashboard',name=patient.name)
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')

        except patientSignUp.DoesNotExist:
            # Patient with given email does not exist
            messages.error(request, 'Patient with this email does not exist.')
    return render(request, 'patient/patient_login.html')

#---------------Doctor Login View-----------------------------------------
def dlogin(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            # Retrieve patient based on mobile
            doctor = doctorSignUp.objects.get(mobile=mobile)

            if doctor.password == password:
                # Password matches, log in user
                # Here, you might want to consider using Django's built-in authentication system
                return redirect('ddashboard',name=doctor.name)  # Replace 'ddashboard' with your actual dashboard URL name
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')

        except doctorSignUp.DoesNotExist:
            # Patient with given email does not exist
            messages.error(request, 'Patient with this email does not exist.')
    return render(request, 'doctor/doctor_login.html')

#---------------Receptionist Login View-----------------------------------------
def rlogin(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            # Retrieve patient based on mobile
            recp = receptionistSignUp.objects.get(mobile=mobile)

            if recp.password == password:
                # Password matches, log in user
                # Here, you might want to consider using Django's built-in authentication system
                return redirect('rdashboard')  # Replace 'rdashboard' with your actual dashboard URL name
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')

        except receptionistSignUp.DoesNotExist:
            # receptionist with given n umber does not exist
            messages.error(request, 'receptionist with this mobile number does not exist.')
    return render(request, 'receptionist/receptionist_login.html')


#---------------Lab Technician Login View-----------------------------------------
def llogin(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            # Retrieve patient based on mobile
            lb = labtechnicianSignUp.objects.get(mobile=mobile)

            if lb.password == password:
                # Password matches, log in user
                # Here, you might want to consider using Django's built-in authentication system
                return redirect('ldashboard')  # Replace 'ldashboard' with your actual dashboard URL name
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')

        except labtechnicianSignUp.DoesNotExist:
            # lab technician with given mobile number does not exist
            messages.error(request, 'lab technician with this mobile number does not exist.')
    return render(request, 'lab_technician/lab_technician_login.html')

#---------------Admin Login View-----------------------------------------
def alogin(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            # Retrieve patient based on mobile
            doctor = adminSignUp.objects.get(mobile=mobile)

            if doctor.password == password:
                # Password matches, log in user
                # Here, you might want to consider using Django's built-in authentication system
                return redirect('adashboard')  # Replace 'pdashboard' with your actual dashboard URL name
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')

        except adminSignUp.DoesNotExist:
            # Admin with given mobile number does not exist
            messages.error(request, 'Admin with this mobile number does not exist.')
    return render(request, 'admin/admin_login.html')


#-------------Patient Success Page View----------------------------------------------
def psuccess(request):
    if request.method == 'POST':
      return redirect('plogin')
    return render(request, 'success/psuccess.html')

#-------------Doctor Success Page View----------------------------------------------
def dsuccess(request):
    if request.method == 'POST':
      return redirect('dlogin')
    return render(request, 'success/dsuccess.html')

#-------------Receptionist Success Page View----------------------------------------------
def rsuccess(request):
    if request.method == 'POST':
      return redirect('rlogin')
    return render(request, 'success/rsuccess.html')

#-------------Lab Technician Success Page View----------------------------------------------
def lsuccess(request):
    if request.method == 'POST':
      return redirect('llogin')
    return render(request, 'success/lsuccess.html')

#-------------Admin Success Page View----------------------------------------------
def asuccess(request):
    if request.method == 'POST':
      return redirect('alogin')
    return render(request, 'success/asuccess.html')

#-------------Patient Dashboard Page View----------------------------------------------
def pdashboard(request,name):
    patient=patientSignUp.objects.get(name=name)
    return render(request, 'patient/patient_dashboard.html',{'patient_name':name,'patient_age':patient.age})

#--------------Display Doctors ----------------------------------------------------------
def pdoctor(request,name):
    doctors = doctorSignUp.objects.all()
    return render(request,'patient/pdoctor.html',{'patient_name':name,'doctors':doctors})

#--------------Display Hospitals ----------------------------------------------------------
def phospital(request,name):
    hospitals = doctorSignUp.objects.all().distinct()
    unique_hospitals = []
    seen_hospitals = set()
    
    for hospital in hospitals:
        if hospital.hname not in seen_hospitals:
            seen_hospitals.add(hospital.hname)
            unique_hospitals.append(hospital)
    return render(request,'patient/phospital.html',{'patient_name':name,'hospitals':unique_hospitals})

#--------------Display Selected Hospital Doctors ----------------------------------------------------------
def doctors_list(request,name,hname):
    doctor= doctorSignUp.objects.filter(hname=hname)
    return render(request,'patient/selecteddoctors.html',{'patient_name':name,'hname':hname, 'doctors':doctor})

#--------------Book Appointments ----------------------------------------------------------
def book_appointment(request, doctor_id, name):
    patient=patientSignUp.objects.get(name=name)
    doctor = get_object_or_404(doctorSignUp, id=doctor_id)
    time_slots = timeSlot.objects.filter(doctor=doctor).order_by('date', 'time')
    
    # Categorize time slots
    categorized_slots = {
        'morning': [],
        'afternoon': [],
        'evening': []
    }

    for slot in time_slots:
        if slot.time < datetime.time(12, 0):
            categorized_slots['morning'].append(slot)
        elif slot.time < datetime.time(18, 0):
            categorized_slots['afternoon'].append(slot)
        else:
            categorized_slots['evening'].append(slot)

    context = {
        'patient_name':patient.name,
        'doctor': doctor,
        'categorized_slots': categorized_slots
    }

    return render(request, 'patient/book_appointment.html', context)

#--------------Update patient Details-----------------------------------------------------------------
def pupdate(request, name):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        # Debug statements to print out the received form data
        print(f"Email: {email}")
        print(f"Mobile: {mobile}")
        print(f"Address: {address}")
        print(f"Profile Pic: {profile_pic}")

        # Check for missing email
        if not email:
            messages.error(request, 'Email field is required.')
            return redirect('pupdate', name=name)

        try:
            patient = patientSignUp.objects.get(name=name)
            patient.email = email
            patient.mobile = mobile
            patient.address = address
            if profile_pic:
                patient.profile_pic = profile_pic
            patient.save()
            messages.success(request, 'Profile updated successfully.')
            patient.save()
            return redirect('pdashboard', name=name)
        except patientSignUp.DoesNotExist:
            messages.error(request, 'Patient does not exist.')
            return redirect('pupdate', name=name)
    else:
        try:
            patient = patientSignUp.objects.get(name=name)
            return render(request, 'patient/pupdate.html', {'patient_name':patient.name,'patient': patient})
        except patientSignUp.DoesNotExist:
            messages.error(request, 'Patient does not exist.')
            return redirect('pupdate', name=name)


#-------------Doctor Dashboard Page View----------------------------------------------
def ddashboard(request,name):
    doctor=doctorSignUp.objects.get(name=name)
    return render(request, 'doctor/doctor_dashboard.html',{'doctor_name':name,'specialist':doctor.specialist,'hname':doctor.hname})

def dtimeslots(request,name):
    doctor=doctorSignUp.objects.get(name=name)
    if request.method == 'POST':
      try:
        date = request.POST['date']
        time = request.POST['time']
        max_appointments = request.POST['max_appointments']
      except MultiValueDictKeyError:
            return render(request, 'doctor/dtimeslots.html', {
                'error': 'Please fill in all fields.',
                'doctor_name': doctor.name,
                'specialist': doctor.specialist,
                'hname': doctor.hname
            })

      new_timeslot = timeSlot(
            doctor=doctor,
            date=date,
            time=time,
            max_appointments=max_appointments
        )
      new_timeslot.save()
        
      return render(request, 'doctor/dtimeslots.html', {'success': True,'doctor_name':name,'specialist':doctor.specialist,'hname':doctor.hname})
    return render(request, 'doctor/dtimeslots.html', {'success': False,'doctor_name':name,'specialist':doctor.specialist,'hname':doctor.hname})

#-------------Receptionist Dashboard Page View----------------------------------------------
def rdashboard(request):
    return render(request, 'receptionist/receptionist_dashboard.html')

#-------------Lab Technician Dashboard Page View----------------------------------------------
def ldashboard(request):
    return render(request, 'lab_technician/lab_technician_dashboard.html')

#-------------Admin Dashboard Page View----------------------------------------------
def adashboard(request):
    return render(request, 'admin/admin_dashboard.html')
