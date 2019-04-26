'''
Manages the translation system.

Last update: 26/04/19
'''
# Dependancies
import gettext, asyncio, time

from data.queries.select.user_info import User_language

async def Translator(client, ctx):
    '''
    This function returns the right translated strings in function of the user's language

    Return: str
    '''
    caller = ctx.message.author
    caller_lang = await User_language(client, caller)
    if(type(caller_lang) == str):
        caller_lang = caller_lang.upper()
    else:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in cogs.utils.translation.translation.Translator : The \'caller_lang\' type is uncorrect'.format(error_time))
        return

    # Get the translations
    if(caller_lang == 'FR'):
        # French translation
        french_t = gettext.translation('fr', localedir= 'locale', languages= ['fr'])
        french_t.install()

        # The '_' will be the function used to translate different strings
        _ = french_t.gettext
        
        return(_)
    
    # If the language is the default language ('EN') we don't translate anything
    else:
        gettext.install('locale/pantheist_translation')

        _ = gettext.gettext

        return(_)