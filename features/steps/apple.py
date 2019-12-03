from behave import given, when, then
from ptest.assertion import assert_equals

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):  # 参数名字可以随便定义
    print('1')
    pass

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    print('2')
    pass

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    print('dddd')