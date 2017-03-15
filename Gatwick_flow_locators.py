from qatools.pageobjects.element import Element
from qatools.pageobjects.page import Page
import datetime

locators = {
    'journey':              'Gatwick Airport to London Victoria',
    'arriveDepart':         'Leaving at',
    'hours':                '13',
    'minutes':              '30',
    "stationCollection":    'London Victoria',
    "firstname":            'Christophe',
    "surname":              'Bailleul',
    "email_increment":      '21',
    "password":             'totototo',
    "address":              '30 Great Guildford street',
    "towncity":             'London',
    "postcode":             'SE1 0HS',
    "cardNumber":           '9902000000005132',
    "expiryMonth":          '12',
    "expiryYear":           '2020',
    "cv2":                  '234',
    "contactPhoneNumber":   '07508501409',
    "title":                'Mr',
    "cardnickname":         'my_test_card',

}

def get_email():
    datenow = datetime.datetime.now()
    return "{}.{}+{}@ontrackretail.co.uk".format(locators["firstname"], locators["surname"], datenow.strftime("%m%d%H%M%S"))

def get_change_month():
    day_month_now_day_delta = []
    datenow = datetime.datetime.now()
    # 0: day
    day_month_now_day_delta.append(int(datenow.strftime("%e")))
    # 1: month
    day_month_now_day_delta.append(int(datenow.strftime("%m")))
    leavingdate = datetime.datetime.now() + datetime.timedelta(weeks = 2)
    # 2: day
    day_month_now_day_delta.append(int(leavingdate.strftime("%e")))
    # 3: month
    day_month_now_day_delta.append(int(leavingdate.strftime("%m")))
    return day_month_now_day_delta


class LoginPage(Page):

    def check_on_load(self):
        return [LoginPage.username,
                LoginPage.password,
                LoginPage.login_validation]

    class username(Element):
        loc = "id", "username"

    class password(Element):
        loc = "id", "password"

    class login_validation(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]"

class RegisterPage(Page):

    def check_on_load(self):
        return [RegisterPage.title,
                RegisterPage.firstName,
                RegisterPage.surname,
                RegisterPage.email,
                RegisterPage.emailConfirm,
                RegisterPage.password,
                RegisterPage.contactPhoneNumber,
                RegisterPage.boxtextmarketing,
                RegisterPage.boxemailmarketing,
                RegisterPage.validate_button
                ]

    class title(Element):
            loc = "id", "title"

    class firstName(Element):
        loc = "id", "firstName"

    class surname(Element):
        loc = "id", "surname"

    class email(Element):
        loc = "id", "email"

    class emailConfirm(Element):
        loc = "id", "confirmemail"

    class password(Element):
        loc = "id", "password"

    class confirmpassword(Element):
        loc = "id", "confirmPassword"

    class contactPhoneNumber(Element):
        loc = "id", "contactPhoneNumber"

    class boxtextmarketing(Element):
        loc = "id", "smsMarketing"

    class boxemailmarketing(Element):
        loc = "id", "emailMarketing"

    class existingemail(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[2]/section/div/div/div[1]/p"

    class validate_button(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]"


class SuccessRegistrationPage(Page):

    def check_on_load(self):
        return [SuccessRegistrationPage.successmessage,
                SuccessRegistrationPage.validation_button]

    class successmessage(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/p"

    class validation_button(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button"

class SearchPage(Page):

    def check_on_load(self):
        return [SearchPage.journey,
                SearchPage.departure_tomorrow,
                SearchPage.arriveDepart_outbound,
                SearchPage.hours_outbound,
                SearchPage.minutes_outbound,
                SearchPage.passengermenu]

    class login_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]"

    class loggedin(Element):
        loc = "xpath", "//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button"

    class register_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[2]"

    class journey(Element):
        loc = "id", "journey"

    class departure_tomorrow(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[1]/button[2]"

    class arriveDepart_outbound(Element):
        loc = "id", "arriveDepart"

    class hours_outbound(Element):
        loc = "id", "hours"

    class minutes_outbound(Element):
        loc = "id", "minutes"

    class add_return_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/button"

    class cal_return_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/div/div[1]/div[2]/button"

    class arriveDepart_return(Element):
        loc = "id", "arriveDepart"

    class hours_return(Element):
        loc = "id", "hours"

    class minutes_return(Element):
        loc = "id", "minutes"

    class next_month(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[2]/div/div/div[1]/button[3]"

    class return_day(Element):
        depart_day = get_change_month()
        depart_day[3] -= 1
        loc = "xpath", "//*[@id='rw_3_calendar__month_{}-{}']".format(depart_day[3], depart_day[2])

    class passengermenu(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section[3]/button"

    class find_trains(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/footer/button"


class PassengersPage(Page):

    def check_on_load(self):
        return [PassengersPage.passengerselection]

    class passengerselection(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]"

    class add_adult(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[2]/section/div[1]/div/div[1]/div/button[2]/i"


class OutboundservicePage(Page):

    def check_on_load(self):
        return [OutboundservicePage.continue_button]

    class outbound_service_selection(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[2]/div/div[1]/div[2]/div/button"

    class continue_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]"



class TicketPage(Page):

    def check_on_load(self):
        return [TicketPage.continue_button,
                TicketPage.cancel_button]

    class continue_button(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]"

    class cancel_button(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[1]"

    class journey_ticket(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[2]/div[2]/div/ul/li[3]/label/div[2]/div"

    class show_ticket_details(Element):
        loc = "xpath", "/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div/ul/li/button"


class ReturnservicePage(Page):

    def check_on_load(self):
        return [ReturnservicePage.continue_button]

    class return_service_selection(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[2]/div/div[1]/div[2]/div/button"

    class continue_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]"


class CollectionPage(Page):

    def check_on_load(self):
        return [CollectionPage.basket,
                CollectionPage.collect_station]

    class collect_station(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div[3]/div/label/span/span/span[1]"

    class basket(Element):
        loc = "xpath", "//*[@id='container']/div/div/header/nav[2]/ul/li[1]/div/button/span[2]/span[1]"

    class stationselect(Element):
        loc = "id", "stationselect"

    class payment_details(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[3]/div[2]/button"


class PaymentPage(Page):

    def check_on_load(self):
        return [PaymentPage.payment_method,
                PaymentPage.payment_button]

    class payment_method(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div[2]/div[2]"

    class payment_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[3]/div[2]/button"

    class evouchers(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div[1]/div[3]/div/div/label/span"

    class existing_card(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div[2]/div[2]/div[1]/div/div/label/span"

    class save_card(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div[2]/div[2]/div[3]/div/div/label/span"

    class cardnickname(Element):
        loc = "id", "nickname"

    class cardHolderName(Element):
        loc = "id", "cardHolderName"

    class cardNumber(Element):
        loc = "id", "cardNumber"

    class expiryMonth(Element):
        loc = "id", "expiryMonth"

    class expiryYear(Element):
        loc = "id", "expiryYear"

    class cv2(Element):
        loc = "id", "cvv"

    class addressline1(Element):
        loc = "id", "addressline1"

    class towncity(Element):
        loc = "id", "towncity"

    class postcode(Element):
        loc = "id", "postcode"

    class email(Element):
        loc = "id", "email"

    class emailConfirm(Element):
        loc = "id", "emailConfirm"

    class contactPhoneNumber(Element):
        loc = "id", "contactPhoneNumber"

    class password(Element):
        loc = "id", "password"

    class title(Element):
        loc = "id", "title"

    class firstName(Element):
        loc = "id", "firstName"

    class surname(Element):
        loc = "id", "surname"

    class messagemarketing(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div[2]/div[3]/div/div[5]/div[2]/div[2]"

    class boxMarketing(Element):
        loc = "id", "emailMarketing"

    class spanMarketing(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/form/div[2]/div[3]/div/div[5]/div[2]/div[2]/div/div/div/div/label/span"

    class payment_button(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]"

    class pay360acsframe(Element):
        loc = "name", "iframe"

    class pay360acsauthorise(Element):
        loc = "xpath", "//*[@id='submitForm']/div[1]/input[1]"

    class pay360acsresume_content(Element):
        loc = "id", "advanced1"

class paymentDetailsPage(Page):

    def check_on_load(self):
        return [paymentDetailsPage.transactionnumber]

    class transactionnumber(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/div[1]/div/div/p[2]"

    class basket(Element):
        loc = "xpath", "//*[@id='container']/div/div/header/nav[2]/ul/li[1]/div/button/span[2]/span[1]"

    class amount(Element):
        loc = "xpath", "//*[@id='container']/div/div/section/div/div[1]/section/div/div[1]/div/div/ul/li/span/strong/span"


def check_element_inheritance(element):
    return eval(element.expected_page_name + "." + element.element_name)
