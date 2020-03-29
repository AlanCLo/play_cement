from cement import Controller, ex



class World(Controller):
    class Meta:
        label = 'world'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(help='test this function')
    def test(self):
        print('Hello world')


    @ex(
        help='huh',
        arguments=[
            ( ['item_text'],
              {'help': 'enter some text',
               'action': 'store' } ),
            ( ['--arg2'],
              {'help': 'named arg',
               'action': 'store',
               'dest': 'named_arg' } ),
        ],
    )
    def huh(self):
        item_text = self.app.pargs.item_text
        named_arg = self.app.pargs.named_arg
        print(f"item_text: {item_text}")
        if named_arg:
            print(f"named_arg: {named_arg}")


    @ex(
        help='What about jinja?',
        arguments=[
            ( ['item1'],
              {'help': 'First',
               'action': 'store' } ),
            ( ['item2'],
              {'help': 'Second',
               'action': 'store' } ),
        ],
    )
    def jinja_test(self):
        data = {}
        data['item1'] = self.app.pargs.item1
        data['item2'] = self.app.pargs.item2
        self.app.render(data, 'jinja_test.jinja2')
