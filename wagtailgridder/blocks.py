from wagtail.wagtailcore.blocks import (
    StructBlock,
    StreamBlock,
    TextBlock,
)
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class DocumentActionItemBlock(StructBlock):
    label = TextBlock(required=True)
    document = DocumentChooserBlock(required=True)

    class Meta:
        icon = 'fa-file'
        template = 'blocks/document_action_item.html'
        help_text = 'Select a document and label for the button.'


class URLActionItemBlock(StructBlock):
    label = TextBlock(required=True)
    url = TextBlock(required=True)

    class Meta:
        icon = 'fa-link'
        template = 'blocks/url_action_item.html'
        help_text = 'Select a URL and label for the button.'


class PlaceholderBlock(StructBlock):
    pass

    class Meta:
        icon = 'fa-square-o'
        template = 'blocks/placeholder_action_item.html'
        help_text = 'Empty placeholder to align buttons in rows.'


class ActionItemStreamBlock(StreamBlock):
    document_button = DocumentActionItemBlock(icon='fa-file')
    url_button = URLActionItemBlock(icon='fa-link')
    placeholder = PlaceholderBlock(icon='fa-square-o')


class ButtonSectionBlock(StructBlock):
    action_items = ActionItemStreamBlock(help_text='A button or URL within a button section.')

    class Meta:
        icon = 'fa-list'
        template = 'blocks/button_section.html'
        help_text = 'Sections divide the action item area into rows.'


class ButtonBlock(StreamBlock):
    button_section = ButtonSectionBlock()

    class Meta:
        help_text = "A row of buttons in the expanded grid item area."
