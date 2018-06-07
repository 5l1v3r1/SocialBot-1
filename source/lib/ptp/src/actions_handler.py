from fuzzywuzzy import fuzz


class ActionsHandler:
    """
    actions object function:

    There are 3 different cases that a text could match.
        1:
            A text contains exactly the text specified in a exactly attribute.
        2:
            A text matches with a text specified in a match attribute, by more or exactly the
            percentage specified in the accuracy attribute.
        3:
            A text contains all words specified in the tags attribute.

    If the case matches the action is returned.
    """

    @staticmethod
    def check_and_sort_actions(actions):
        """
        Check the content of a actions object.
        :param actions:
        :return:
        """

        exactly = []
        match = []
        tags = []

        for a in actions:
            keys = a.keys()

            if 'exactly' not in keys and 'match' not in keys and 'tags' not in keys:
                raise ValueError('The actions dict is missing either the exactly, match or tags key.', str(a))
            elif 'exactly' in keys and not a['exactly']:
                raise ValueError('Found exactly key, but it has no content.', str(a))
            elif 'match' in keys and not a['match']:
                raise ValueError('Found match key, but it has no content.', str(a))
            elif 'tags' in keys:
                if len(a['tags']) == 0:
                    raise ValueError('Found tags key, but it has no content.', str(a))
                else:
                    for item in a['tags']:
                        if not item or type(item) != str:
                            raise ValueError('Tags key, has no or wrong content (has to be str).', str(a))

            if 'action' not in keys or not a['action']:
                raise ValueError('Missing a action key.', str(a))
            elif 'action' in keys:
                ac = a['action']

                if type(ac) == str:
                    if ac == 'reply':
                        if 'text' not in keys or not a['text']:
                            raise ValueError('Missing a text key for action reply.', str(a))
                    elif ac != 'retweet' and ac != 'favor' and ac != 'follow':
                        raise ValueError(
                            'Found a action key, but it has no or wrong content (not reply, retweet, favor or follow).',
                            str(a)
                        )
                elif type(ac) == list:
                    act_list = ['reply', 'favor', 'retweet', 'follow']

                    for item in act_list:
                        if ac.count(item) > 1:
                            raise ValueError('Only one of every type of action should be in the action list.', str(a))

                    if 'reply' in ac:
                        if 'text' not in keys or not a['text']:
                            raise ValueError('Missing a text key for a action reply.', str(a))

                    for item in a['action']:
                        if item not in act_list:
                            raise ValueError(
                                'Found a action key, but there is wrong content in the action list (not reply, '
                                'retweet, favor or follow)',
                                str(a)
                            )
                else:
                    raise ValueError('The action has to be of type str or list. Found:', type(a['action']))

            if 'match' in keys and 'accuracy' not in keys:
                raise ValueError('Found match key, missing a accuracy key.', str(a))
            elif 'accuracy' in keys and (not a['accuracy'] or a['accuracy'] > 1):
                raise ValueError('Found accuracy key, but it has no or wrong content (> 1).', str(a))

            if 'options' in keys:
                opt_keys = a['options'].keys()

                if 'case_sensitive' not in opt_keys:
                    raise ValueError('Unknown key found in options.', str(opt_keys), str(a))
                elif type(a['options']['case_sensitive']) != bool:
                    raise ValueError('Case_sensitive value has to be of type bool.', str(a))

            if 'exactly' in keys and 'action' in keys:
                exactly.append(a)
            elif 'match' in keys and 'accuracy' in keys and 'action' in keys:
                match.append(a)
            elif 'tags' in keys and len(a['tags']) > 0 and 'action' in keys:
                tags.append(a)

        return {
            'exactly': exactly,
            'match': match,
            'tags': tags
        }

    @staticmethod
    def find_action(f_actions, text):
        """
        Finds action to react to a text.
        :param f_actions:
        :param text:
        :return:
        """

        exactly_list = f_actions['exactly']
        match_list = f_actions['match']
        tags_list = f_actions['tags']
        matched_action = None

        for entry in exactly_list:
            if 'options' in entry and 'case_sensitive' in entry['options'] and entry['options']['case_sensitive']:
                if text == entry['exactly']:
                    matched_action = entry
                    break
            else:
                if text.lower() == entry['exactly'].lower():
                    matched_action = entry
                    break

        if not matched_action:
            for entry in match_list:
                if 'options' in entry and 'case_sensitive' in entry['options'] and entry['options']['case_sensitive']:
                    if (fuzz.ratio(text, entry['match']) / 100) > entry['accuracy']:
                        matched_action = entry
                        break
                else:
                    if ((fuzz.ratio(text.lower(), entry['match'].lower()) / 100) >
                            entry['accuracy']):
                        matched_action = entry
                        break

        if not matched_action:
            for entry in tags_list:
                every_tag = True
                if 'options' in entry and 'case_sensitive' in entry['options'] and entry['options']['case_sensitive']:
                    for tag in entry['tags']:
                        if tag not in text:
                            every_tag = False
                            break
                else:
                    for tag in entry['tags']:
                        if tag.lower() not in text.lower():
                            every_tag = False
                            break
                if every_tag:
                    matched_action = entry
                    break

        return matched_action
