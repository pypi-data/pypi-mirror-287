# MkdocsExternalLinkProcessor

The `MkdocsExternalLinkProcessor` is an [MkDocs](https://mkdocs.org) plugin designed to enhance the handling of external links in your documentation. It allows you to add specific CSS classes, set the `target` attribute, and configure the `rel` attribute for external links.

## Features

- **Add Class to External Links**: Automatically add a specified CSS class to all external links.
- **Configure Link Target**: Set the `target` attribute (e.g., `_blank`) to control how links open.
- **Configure Link Rel Attribute**: Set the `rel` attribute for external links for improved security and SEO.
- **Custom Protocols**: Extend the default list of protocols to include additional ones.

## Installation

To install the plugin, include it in your MkDocs project by placing the `mkdocs_external_link_processor.py` file in your project and adding it to your `mkdocs.yml` configuration file.

1. Save the plugin file as `mkdocs_external_link_processor.py`.
2. Add the plugin to your `mkdocs.yml` configuration:
```yaml
plugins:
  - mkdocs_external_link_processor
```

## Configuration

You can configure the plugin by adding the following options to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs_external_link_processor:
      class_name: 'external'                # Class name to add to external links
      link_target: '_blank'                 # Target attribute for links
      link_rel: ['noopener', 'noreferrer']  # Rel attribute for links
      additional_protocols: ['custom:']     # Additional protocols to consider as external
```

### Configuration Options

- **`class_name`**: The CSS class to add to external links. Defaults to `'external'`.
- **`link_target`**: The `target` attribute for links. Use `'_blank'` to open links in a new tab. Defaults to an empty string.
- **`link_rel`**: The `rel` attribute values to apply to links. Defaults to an empty list.
- **`additional_protocols`**: Additional protocols to consider as external links. Defaults to an empty list.

## Usage

After configuring the plugin, it will automatically process the links in your documentation:

1. **Add Class**: All external links will have the specified class added.
2. **Set Target**: The `target` attribute will be set according to your configuration.
3. **Set Rel**: The `rel` attribute will be added to external links.

## Example

Given the following HTML content:

```html
<a href="https://example.com">Example</a>
<a href="mailto:contact@example.com">Contact</a>
<a href="custom:protocol">Custom Protocol</a>
```

With the configuration:

```yaml
plugins:
  - mkdocs_external_link_processor:
      class_name: 'external'
      link_target: '_blank'
      link_rel: ['noopener', 'noreferrer']
      additional_protocols: ['custom:']
```

The resulting HTML will be:

```html
<a href="https://example.com" class="external" target="_blank" rel="noopener noreferrer">Example</a>
<a href="mailto:contact@example.com" class="external" target="_blank" rel="noopener noreferrer">Contact</a>
<a href="custom:protocol" class="external" target="_blank" rel="noopener noreferrer">Custom Protocol</a>
```

## Development

To contribute to the development of this plugin, clone the repository and make your changes. Ensure that you have `BeautifulSoup` installed:

```bash
pip install beautifulsoup4
```

## License

This project is licensed under the [MIT License](LICENSE.md)
