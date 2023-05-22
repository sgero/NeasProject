from django.forms.widgets import Widget
from django.utils.html import format_html

class StarRatingWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        html = ''
        for i in range(1, 6):
            checked = '' if value != i else 'checked'
            html += f'{i}<input type="radio" name="{name}" value="{i}" {checked} required/><i class="fa fa-star"></i>'
        return format_html(html)