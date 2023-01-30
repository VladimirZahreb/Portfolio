import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, ToolTipsPage, MenuPage

"""Testing different widgets on the site page"""

class TestWidgets:

    """Testing widget "Accordian on the site page"""

    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            # time.sleep(3)
            first_title, first_content = accordian_page.check_accordian('first')
            # time.sleep(3)
            second_title, second_content = accordian_page.check_accordian('second')
            # time.sleep(3)
            third_title, third_content = accordian_page.check_accordian('third')
            # time.sleep(3)
            # print(first_title, first_content)
            # print(second_title, second_content)
            # print(third_title, third_content)
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePage:

        """Testing widget "Auto Complete" on the site page"""

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            time.sleep(3)
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            print(colors)
            print(colors_result)
            assert colors == colors_result, 'the added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            # time.sleep(5)
            autocomplete_page.remove_value_from_multi()
            # time.sleep(5)
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            # print(count_value_before)
            # print(count_value_after)
            assert count_value_before != count_value_after, "value was not deleted"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            # print(color)
            # print(color_result)
            assert color == color_result, 'the added colors are missing in the input'

    class TestDatePickerPage:

        """Testing widget "Date Picker" on the site page"""

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'the date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date = date_picker_page.select_date()
            # print(date)
            value_date_before, value_date_after = date_picker_page.select_date()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'the date and time have not been changed'

    class TestSliderPage:

        """Testing widget "Slider" on the site page"""

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, 'the slider value has not been changed'

    class TestProgressBarPage:

        """Testing widget "Progress Bar" on the site page"""

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, 'the progress bar value has not been changed'

    class TestTabsPage:

        """Testing widget "Tabs" on the site page"""

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'
            assert more_button == 'More' and what_content != 0, 'the tab "more" was not pressed or the text is missing'

    class TestToolTips:

        """Testing widget "Tool Tips" on the site page"""

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    class TestMenuPage:

        """Testing widget ""Menu" on the site page"""

        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "menu items do not exist or have not been selected"
