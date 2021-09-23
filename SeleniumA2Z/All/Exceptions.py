from selenium import webdriver
from selenium.common.exceptions import WebDriverException, RemoteDriverServerException, TimeoutException, \
    ScreenshotException, JavascriptException, NoSuchCookieException, NoSuchElementException, NoSuchWindowException, \
    ElementNotSelectableException, ElementNotInteractableException, StaleElementReferenceException, \
    ElementClickInterceptedException, InvalidElementStateException, InvalidCoordinatesException, \
    ElementNotVisibleException, ImeNotAvailableException, SessionNotCreatedException, InvalidSessionIdException, \
    InvalidArgumentException, InvalidSelectorException, InvalidCookieDomainException, InvalidSwitchToTargetException, \
    UnableToSetCookieException, UnknownMethodException, NoSuchFrameException, NoSuchAttributeException, \
    NoAlertPresentException, UnexpectedAlertPresentException, UnexpectedTagNameException, ErrorInResponseException, \
    ImeActivationFailedException, InsecureCertificateException, MoveTargetOutOfBoundsException

try:
    driver = webdriver.Chrome()
except (WebDriverException, RemoteDriverServerException, TimeoutException, ScreenshotException, JavascriptException,
        NoSuchCookieException, NoSuchElementException, NoSuchWindowException,
        ElementNotSelectableException, ElementNotInteractableException, StaleElementReferenceException,
        ElementClickInterceptedException, InvalidElementStateException, InvalidCoordinatesException,
        ElementNotVisibleException, ImeNotAvailableException, SessionNotCreatedException, InvalidSessionIdException,
        InvalidArgumentException, InvalidSelectorException, InvalidCookieDomainException,
        InvalidSwitchToTargetException,
        UnableToSetCookieException, UnknownMethodException, NoSuchFrameException, NoSuchAttributeException,
        NoAlertPresentException, UnexpectedAlertPresentException, UnexpectedTagNameException, ErrorInResponseException,
        ImeActivationFailedException, InsecureCertificateException, MoveTargetOutOfBoundsException):
    print('')
