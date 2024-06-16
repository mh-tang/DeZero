# step 23: simple core
is_simple_core = True


if is_simple_core:
    from dezero.core_simple import Variable
    from dezero.core_simple import Function
    from dezero.core_simple import using_config
    from dezero.core_simple import no_grad
    from dezero.core_simple import as_array
    from dezero.core_simple import as_variable
    from dezero.core_simple import setup_variable


setup_variable()  # 重载Variable类的一些属性
__version__ = '0.2.24'  # version.stage.step