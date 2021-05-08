from stuff.files_path import files_path


def capability_select():
    capability = {"platformName": "Android",
                  "platformVersion": "8.1",
                  "automationName": "Appium",
                  "appPackage": "ru.mail.search.electroscope",
                  "app": files_path("Marussia_v1.39.1.apk"),
                  "orientation": "PORTRAIT",
                  "autoGrantPermissions": "true"
                  }
    return capability
