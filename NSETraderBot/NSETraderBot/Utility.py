from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from email.message import EmailMessage
from NSETraderBot import ConstURLList
import six, json, re, smtplib, os, imghdr

generalurls = ConstURLList.GeneralURLList()


class TraderUtility:

    def nse_headers(self):
        return {'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Host': 'www1.nseindia.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                'X-Requested-With': 'XMLHttpRequest'
                }

    def nse_opener(self):
        cj = CookieJar()
        return build_opener(HTTPCookieProcessor(cj))

    def byte_adaptor(self, fbuffer):
        strings = fbuffer.read().decode('latin-1')
        fbuffer = six.StringIO(strings)
        return fbuffer

    def render_response(self, data, as_json=False):
        if as_json is True:
            return json.dumps(data)
        else:
            return data

    def clean_server_response(self, resp_dict):
        d = {}
        for key, value in resp_dict.items():
            d[str(key)] = value
        resp_dict = d
        for key, value in resp_dict.items():
            if type(value) is str or isinstance(value, six.string_types):
                if re.match('-', value):
                    try:
                        if float(value) or int(value):
                            dataType = True
                    except ValueError:
                        resp_dict[key] = None
                elif re.search(r'^[0-9,.]+$', value):
                    resp_dict[key] = float(re.sub(',', '', value))
                else:
                    resp_dict[key] = str(value)
        return resp_dict


class GeneralUtility:

    def sendmailutility(self, argSendToLst, argSubject, argHTMLContent, argattachmentfiles, argMailType):
        try:
            rtnmailsent = False
            EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
            EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
            image_type = ['JPEG', 'JPG', 'PNG', 'GIF', 'TIFF', 'PSD', 'PDF', 'RAW']
            pdf_type = ['PDF']
            smtp_url = generalurls.getGmailSMTP

            # Todo Need to add a switch like statement to identify the type of mail send from for SMTP -- (argMailType)
            # Todo Need to configure for different_type(gmail,outlook all at once) of send email addresses for SMTP

            mail_message = EmailMessage()
            mail_message['From'] = EMAIL_ADDRESS
            mail_message['Subject'] = argSubject

            if not isinstance(argSendToLst, list):
                raise TypeError("argument argSendToLst/ To should be a list")
            mail_message['To'] = argSendToLst

            if argHTMLContent != None:
                mail_message.set_content("This is a plain text email")
                mail_message.add_alternative(argHTMLContent, subtype='html')

            if argattachmentfiles != None:
                for file in argattachmentfiles:
                    with open(file, 'rb') as file_obj:
                        file_data = file_obj.read()
                        file_name = file_obj.name
                        if image_type.contains(imghdr.what(file_obj.name).upper()):
                            file_type = imghdr.what(file_obj.name)
                            mail_message.add_attachment(file_data, maintype='', subtype=file_type, filename=file_name)

                        # TODO Need to add PDF file segregation for attachment
                        # TODO Need to find the file extension
                        # TODO Need to add the  if statement

            with smtplib.SMTP_SSL(smtp_url, 465) as smtp_obj:
                smtp_obj.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp_obj.send_message(mail_message)
            rtnmailsent = True
            return rtnmailsent
        except Exception as ex:
            print(f"Something wrong in sendmailutility in GeneralUtility Exception: {ex}" )
            rtnmailsent = False
            return rtnmailsent