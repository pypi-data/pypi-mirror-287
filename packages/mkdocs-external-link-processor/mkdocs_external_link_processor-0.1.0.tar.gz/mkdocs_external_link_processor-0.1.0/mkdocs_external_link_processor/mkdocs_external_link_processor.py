from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type
from mkdocs.config.base import Config
from bs4 import BeautifulSoup

class MkdocsExternalLinkProcessorConfig(Config):
    """
    Configuration class for MkdocsExternalLinkProcessor.
    
    Attributes:
        class_name (str): The class name to add to external links. Defaults to 'external'.
        link_target (str): The target attribute value for links, e.g., '_blank' to open links in a new tab. Defaults to an empty string.
        link_rel (list): The rel attribute value(s) to apply to links. Defaults to an empty list.
        additional_protocols (list): Additional protocols to consider as external. Defaults to an empty list.
    """
    class_name = Type(str, default='external')
    link_target = Type(str, default='')
    link_rel = Type(list, default=list())
    additional_protocols = Type(list, default=list())

class MkdocsExternalLinkProcessor(BasePlugin[MkdocsExternalLinkProcessorConfig]):
    """
    MkdocsExternalLinkProcessor is a MkDocs plugin that processes HTML content to modify external links.
    
    This plugin adds a specific class to external links, sets the `target` attribute for opening links in a new tab/window,
    and optionally sets the `rel` attribute for those links based on the configuration.

    Attributes:
        class_name (str): The class name to add to external links. Defaults to 'external'.
        link_target (str): The target attribute value for links, e.g., '_blank' to open links in a new tab. Defaults to an empty string.
        link_rel (list): The rel attribute value(s) to apply to links. Defaults to an empty list.
        additional_protocols (list): Additional protocols to consider as external. Defaults to an empty list.
        default_protocols (list): The standard list of protocols to consider as external links. Includes 'http://', 'https://', 'ftp://', 'mailto:', 'tel:', 'www'.
        all_protocols (list): Combination of default_protocols and additional_protocols.

    Methods:
        on_page_content(html: str, page, config, files) -> str:
            Processes the provided HTML content, modifies external links based on the configuration, and returns the updated HTML content.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the MkdocsExternalLinkProcessor plugin.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def on_page_content(self, html: str, page, config, files) -> str:
        """
        Processes HTML content to modify external links.

        This method parses the provided HTML, finds all anchor (`<a>`) tags with `href` attributes, and updates them based on
        the plugin's configuration:
        
        - Adds a specified class to external links.
        - Sets the `target` attribute if configured.
        - Sets the `rel` attribute if configured.

        Args:
            html (str): The HTML content of the page.
            page: The MkDocs page object (not used in this method).
            config: The MkDocs configuration object (not used in this method).
            files: The MkDocs files object (not used in this method).

        Returns:
            str: The modified HTML content with updated external links.
        """
        class_name = self.config.class_name
        target = self.config.link_target
        rel = self.config.link_rel
        additional_protocols = self.config.additional_protocols
        default_protocols = ['http://', 'https://', 'ftp://', 'mailto:', 'tel:', 'www']
        all_protocols = default_protocols + additional_protocols

        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if any(href.startswith(protocol) for protocol in all_protocols):
                if class_name and class_name not in a_tag.get('class', []):
                    classes = a_tag.get('class', [])
                    if not isinstance(classes, list):
                        classes = []
                    a_tag['class'] = classes + [class_name]

            if target:
                a_tag["target"] = target

            if rel:
                a_tag["rel"] = rel

        return str(soup)
