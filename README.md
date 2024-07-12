# academic-org-theme

This is a Jekyll Theme for creating website for academic conferences, groups, and organisations. Having an advanced blog layout page, a complicated landing page, or providing lots of "profile"-style social media links is less important than providing clear and consistent pages.

This theme started out from a basic theme I developed for [my homepage](https://charlesmartin.au), and then for the [NIME community](https://nime.org).

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "academic-org-theme"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: academic-org-theme
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install academic-org-theme

## Usage

TODO: Write usage instructions here. Describe your available layouts, includes, sass and/or assets.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/smcclab/academic-org-theme. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, `_sass` and `assets` tracked with Git will be bundled.
To add a custom directory to your theme-gem, please edit the regexp in `academic-org-theme.gemspec` accordingly.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
