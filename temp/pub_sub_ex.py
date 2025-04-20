from lato import Application, ApplicationModule, Event, Command, TransactionContext

class SampleCommand(Command):
    pass

class FooHappened(Event):
    source: str

foo_module = ApplicationModule(name="foo")
@foo_module.handler(SampleCommand)
def call_foo(command: SampleCommand, ctx: TransactionContext):
    print("handling foo")
    ctx.emit(FooHappened(source="foo"))

bar_module = ApplicationModule(name="bar")
@bar_module.handler(FooHappened)
def on_foo_happened(event: FooHappened):
    print(f"handling event from {event.source}")

@bar_module.handler(FooHappened)
def on_foo_happened_2(event: FooHappened):
    print(f"ЯЯЯ !!! handling event from {event.source}")

foobar = Application()
foobar.include_submodule(foo_module)
foobar.include_submodule(bar_module)

foobar.execute(SampleCommand())
foobar.publish(FooHappened(source="external source"))