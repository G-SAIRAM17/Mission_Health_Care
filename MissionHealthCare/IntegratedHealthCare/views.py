from django.shortcuts import render, redirect
from django.contrib import messages
from .models import patientSignUp
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import random
import string

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
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('psignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('psignup')
            else:
                patientSignUp.objects.create(name=name, age=age, gender=gender, email=email, mobile=mobile, address=address, password=password, reenterpassword=reenterpassword)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi {name}, thank you for registering with us.'
                html_content = f'''
                <!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
  <title> Welcome to Coded Mails </title>
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
  <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Preview - Welcome {name} </div>
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
                        <h1 style="margin: 0; font-size: 24px; line-height: normal; font-weight: bold;"> Welcome Mr/Mrs {name} ! </h1>
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
                      <div style="height:1px;">   </div>
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
<script>
window.onclick= function() {{
  // Globals
  var random = Math.random
    , cos = Math.cos
    , sin = Math.sin
    , PI = Math.PI
    , PI2 = PI * 2
    , timer = undefined
    , frame = undefined
    , confetti = [];

  var particles = 10
    , spread = 40
    , sizeMin = 3
    , sizeMax = 12 - sizeMin
    , eccentricity = 10
    , deviation = 100
    , dxThetaMin = -.1
    , dxThetaMax = -dxThetaMin - dxThetaMin
    , dyMin = .13
    , dyMax = .18
    , dThetaMin = .4
    , dThetaMax = .7 - dThetaMin;

  var colorThemes = [
    function() {{
      return color(200 * random()|0, 200 * random()|0, 200 * random()|0);
    }}, function() {{
      var black = 200 * random()|0; return color(200, black, black);
    }}, function() {{
      var black = 200 * random()|0; return color(black, 200, black);
    }}, function() {{
      var black = 200 * random()|0; return color(black, black, 200);
    }}, function() {{
      return color(200, 100, 200 * random()|0);
    }}, function() {{
      return color(200 * random()|0, 200, 200);
    }}, function() {{
      var black = 256 * random()|0; return color(black, black, black);
    }}, function() {{
      return colorThemes[random() < .5 ? 1 : 2]();
    }}, function() {{
      return colorThemes[random() < .5 ? 3 : 5]();
    }}, function() {{
      return colorThemes[random() < .5 ? 2 : 4]();
    }}
  ];
  function color(r, g, b) {{
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }}

  // Cosine interpolation
  function interpolation(a, b, t) {{
    return (1-cos(PI*t))/2 * (b-a) + a;
  }}

  // Create a 1D Maximal Poisson Disc over [0, 1]
  var radius = 1/eccentricity, radius2 = radius+radius;
  function createPoisson() {{
    // domain is the set of points which are still available to pick from
    // D = union{{ [d_i, d_i+1] | i is even }}
    var domain = [radius, 1-radius], measure = 1-radius2, spline = [0, 1];
    while (measure) {{
      var dart = measure * random(), i, l, interval, a, b, c, d;

      // Find where dart lies
      for (i = 0, l = domain.length, measure = 0; i < l; i += 2) {{
        a = domain[i], b = domain[i+1], interval = b-a;
        if (dart < measure+interval) {{
          spline.push(dart += a-measure);
          break;
        }}
        measure += interval;
      }}
      c = dart-radius, d = dart+radius;

      // Update the domain
      for (i = domain.length-1; i > 0; i -= 2) {{
        l = i-1, a = domain[l], b = domain[i];
        // c---d          c---d  Do nothing
        //   c-----d  c-----d    Move interior
        //   c--------------d    Delete interval
        //         c--d          Split interval
        //       a------b
        if (a >= c && a < d)
          if (b > d) domain[l] = d; // Move interior (Left case)
          else domain.splice(l, 2); // Delete interval
        else if (a < c && b > c)
          if (b <= d) domain[i] = c; // Move interior (Right case)
          else domain.splice(i, 0, c, d); // Split interval
      }}

      // Re-measure the domain
      for (i = 0, l = domain.length, measure = 0; i < l; i += 2)
        measure += domain[i+1]-domain[i];
    }}

    return spline.sort();
  }}

  // Create the overarching container
  var container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.top      = '0';
  container.style.left     = '0';
  container.style.width    = '100%';
  container.style.height   = '0';
  container.style.overflow = 'visible';
  container.style.zIndex   = '9999';

  // Confetto constructor
  function Confetto(theme) {{
    this.frame = 0;
    this.outer = document.createElement('div');
    this.inner = document.createElement('div');
    this.outer.appendChild(this.inner);

    var outerStyle = this.outer.style, innerStyle = this.inner.style;
    outerStyle.position = 'absolute';
    outerStyle.width  = (sizeMin + sizeMax * random()) + 'px';
    outerStyle.height = (sizeMin + sizeMax * random()) + 'px';
    innerStyle.width  = '100%';
    innerStyle.height = '100%';
    innerStyle.backgroundColor = theme();

    outerStyle.perspective = '50px';
    outerStyle.transform = 'rotate(' + (360 * random()) + 'deg)';
    this.axis = 'rotate3D(' +
      cos(360 * random()) + ',' +
      cos(360 * random()) + ',0,';
    this.theta = 360 * random();
    this.dTheta = dThetaMin + dThetaMax * random();
    innerStyle.transform = this.axis + this.theta + 'deg)';

    this.x = window.innerWidth * random();
    this.y = -deviation;
    this.dx = sin(dxThetaMin + dxThetaMax * random());
    this.dy = dyMin + dyMax * random();
    outerStyle.left = this.x + 'px';
    outerStyle.top  = this.y + 'px';

    // Create the periodic spline
    this.splineX = createPoisson();
    this.splineY = [];
    for (var i = 1, l = this.splineX.length-1; i < l; ++i)
      this.splineY[i] = deviation * random();
    this.splineY[0] = this.splineY[l] = deviation * random();

    this.update = function(height, delta) {{
      this.frame += delta;
      this.x += this.dx * delta;
      this.y += this.dy * delta;
      this.theta += this.dTheta * delta;

      // Compute spline and convert to polar
      var phi = this.frame % 7777 / 7777, i = 0, j = 1;
      while (phi >= this.splineX[j]) i = j++;
      var rho = interpolation(
        this.splineY[i],
        this.splineY[j],
        (phi-this.splineX[i]) / (this.splineX[j]-this.splineX[i])
      );
      phi *= PI2;

      outerStyle.left = this.x + rho * cos(phi) + 'px';
      outerStyle.top  = this.y + rho * sin(phi) + 'px';
      innerStyle.transform = this.axis + this.theta + 'deg)';
      return this.y > height+deviation;
    }};
  }}

  function poof() {{
    if (!frame) {{
      // Append the container
      document.body.appendChild(container);

      // Add confetti
      var theme = colorThemes[0]
        , count = 0;
      (function addConfetto() {{
        var confetto = new Confetto(theme);
        confetti.push(confetto);
        container.appendChild(confetto.outer);
        timer = setTimeout(addConfetto, spread * random());
      }})(0);

      // Start the loop
      var prev = undefined;
      requestAnimationFrame(function loop(timestamp) {{
        var delta = prev ? timestamp - prev : 0;
        prev = timestamp;
        var height = window.innerHeight;

        for (var i = confetti.length-1; i >= 0; --i) {{
          if (confetti[i].update(height, delta)) {{
            container.removeChild(confetti[i].outer);
            confetti.splice(i, 1);
          }}
        }}

        if (timer || confetti.length)
          return frame = requestAnimationFrame(loop);

        // Cleanup
        document.body.removeChild(container);
        frame = undefined;
      }});
    }}
  }}

  poof();
}};
</script>

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
        return render(request, 'patient_signup.html')


def plogin(request):
    return render(request, 'patient_login.html')
  
from django.shortcuts import render, redirect

def psuccess(request):
    if request.method == 'POST':
        return redirect('plogin')
    return render(request, 'psuccess.html')
