import pinboard

from pelican import signals

def initialize_pinboard(gen):
    p = pinboard.open(token=gen.settings['PINBOARD_TOKEN'])

    args = dict()
    if 'PINBOARD_COUNT' in gen.settings.keys():
        args['count'] = gen.settings['PINBOARD_COUNT']
    if 'PINBOARD_TAG' in gen.settings.keys():
        args['tag'] = gen.settings['PINBOARD_TAG']

    posts = p.posts(**args)
    gen.context['pinboard_activity'] = posts

def register():
    signals.article_generator_init.connect(initialize_pinboard)
