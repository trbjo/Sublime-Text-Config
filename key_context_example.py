import sublime
import sublime_plugin


class CustomContextEventListener(sublime_plugin.EventListener):
    """
    This event is raised when Sublime sees a key binding context key it does not
    recognize.
    """
    def on_query_context(self, view, key, operator, operand, match_all):
        # Determine if we understand the key. If we don't we should return None
        # to allow Subliem to ask another listener.
        if not key.startswith('view_setting.'):
            return None

        # Obtain the actual setting by removing the common key prefix, and then
        # get the value of the setting for us in our comparison.
        setting = key[len('view_setting.'):]
        lhs = view.settings().get(setting)

        # The operator tells us what sort of comparison to do and the operand
        # is the information that comes from the key binding.
        #
        # The full list of options is:
        #   OP_EQUAL, OP_NOT_EQUAL, OP_REGEX_MATCH, OP_NOT_REGEX_MATCH,
        #   OP_REGEX_CONTAINS, OP_NOT_REGEX_CONTAINS
        if operator == sublime.OP_EQUAL:
            return lhs == operand
        elif operator == sublime.OP_NOT_EQUAL:
            return lhs != operand

        # We understand the key, but someone used an operator that we don't
        # understand, so default to saying that the binding doesn't apply.
        return False
