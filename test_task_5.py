import os

from selene import browser, be, by, have


def test_submit_form(precondition):
    browser.element('input[value="Other"]').double_click()
    browser.element('#firstName').type('Valeryia')
    browser.element('#lastName').type('Kazlova')
    browser.element('#userEmail').type('kazlova@mail.com')
    browser.element('#userNumber').type('3752932112')
    browser.driver.execute_script("document.querySelector('#dateOfBirthInput').scrollIntoView();")
    browser.element('#dateOfBirthInput').click()
    browser.element('select option[value = "4"]').click()
    browser.element('option[value="1986"]').click()
    browser.element('div[class*="028"][aria-label*="May"]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').type(os.getcwd() + '/resources/1570735001190494352.jpg')
    browser.element('#currentAddress').type('Poland, Gdańsk, Wilcza 1')
    browser.driver.execute_script("document.querySelector('#submit').scrollIntoView();")
    browser.element('#state').click().element(by.xpath("//*[.='Haryana']")).click()
    browser.element('#city').click().element(by.xpath("//*[.='Karnal']")).click()
    browser.element('#submit').click()

    browser.element(by.xpath("//div[@class='modal-content']")).should(be.present)
    browser.all('tbody tr').should(
        have.texts(
            'Valeryia Kazlova',
            'kazlova@mail.com',
            'Other',
            '3752932112',
            '28 May,1986',
            'Computer Science',
            'Music',
            '1570735001190494352.jpg',
            'Poland, Gdańsk, Wilcza 1',
            'Haryana Karnal',
        )
    )
