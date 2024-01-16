import os
import pytest
from selenium import webdriver

# def create_screenshot_folder():
#     folder_name = "screenshots"
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#     return folder_name


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    b = webdriver.Chrome(options=options)
    b.implicitly_wait(10)
    yield b
    b.quit()


# def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # print(f'Step failed: {step}')
    # Called when step function failed to execute
    # screenshot_folder = "screenshots"
    # if not os.path.exists(screenshot_folder):
    #     os.makedirs(screenshot_folder)

    # screenshot_name = f"step_{step.name.replace(' ', '_')}_error.png"
    # screenshot_path = os.path.join(screenshot_folder, screenshot_name)

    # request.instance.browser.save_screenshot(screenshot_path)
    # print(f"Screenshot de erro salvo como {screenshot_path}")

# def pytest_bdd_before_scenario(request, feature, scenario)
    # Called before scenario is executed

# def pytest_bdd_before_step(request, feature, scenario, step, step_func)
    # Called before step function is executed and it’s arguments evaluated

# def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args)
    # Called before step function is executed with evaluated arguments

# def pytest_bdd_after_scenario(request, feature, scenario)
    # Called after scenario is executed (even if one of steps has failed)

# def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
#     # Called after step function is successfully executed
#     screenshot_folder = create_screenshot_folder()
#     screenshot_name = f"step_{step.name.replace(' ', '_')}.png"
#     screenshot_path = os.path.join(screenshot_folder, screenshot_name)

#     request.instance.browser.save_screenshot(screenshot_path)
#     print(f"Screenshot salvo como {screenshot_path}")

# def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception)
#     # Called when step function failed to execute

# def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception)
#     # Called when step lookup failed
