---
permalink: /assets/js/search-data.js
---

const ninja = document.querySelector('ninja-keys');

ninja.data = [
  {% assign about_title = '' %}
  {% for page in site.pages %}
    {% if page.permalink == '/' %}
      {% assign about_title = page.title | strip %}
    {% endif %}
  {% endfor %}
  {
    id: "nav-{{ about_title | slugify }}",
    title: "{{ about_title | truncatewords: 13 }}",
    section: "Navigation",
    handler: () => {
      window.location.href = "{{ '/' | relative_url }}";
    },
  },
  {% assign sorted_pages = site.pages | sort: "nav_order" %}
  {% for p in sorted_pages %}
    {% if p.nav and p.autogen == null %}
      {% if p.dropdown %}
        {% for child in p.children %}
          {% unless child.title == 'divider' %}
            {
              id: "dropdown-{{ child.title | escape | strip | slugify }}",
              title: "{{ child.title | escape | strip | truncatewords: 13 }}",
              description: "{{ child.description | strip_html | strip_newlines | escape | strip }}",
              section: "Dropdown",
              handler: () => {
                window.location.href = "{{ child.permalink | relative_url }}";
              },
            },
          {% endunless %}
        {% endfor %}
      {% else %}
        {
          id: "nav-{{ p.title | escape | strip | slugify }}",
          title: "{{ p.title | escape | strip | truncatewords: 13 }}",
          description: "{{ p.description | strip_html | strip_newlines | escape | strip }}",
          section: "Navigation",
          handler: () => {
            window.location.href = "{{ p.permalink | relative_url }}";
          },
        },
      {% endif %}
    {% endif %}
  {% endfor %}
  {% if site.posts_in_search %}
    {% for post in site.posts %}
      {
        id: "post-{{ post.title | escape | strip | slugify }}",
        title: "{% if post.redirect contains '://' %}{{ post.title | truncatewords: 13 }} <svg width='1.2rem' height='1.2rem' top='.5rem' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'><path d='M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9' class='icon_svg-stroke' stroke='#999' stroke-width='1.5' fill='none' fill-rule='evenodd' stroke-linecap='round' stroke-linejoin='round'></path></svg>{% else %}{{ post.title | truncatewords: 13 }}{% endif %}",
        description: "{{ post.description | strip_html | strip_newlines | escape | strip }}",
        section: "Posts",
        handler: () => {
          {% if post.redirect == blank %}
            window.location.href = "{{ post.url | relative_url }}";
          {% elsif post.redirect contains '://' %}
            window.open("{{ post.redirect }}", "_blank");
          {% else %}
            window.location.href = "{{ post.redirect | relative_url }}";
          {% endif %}
        },
      },
    {% endfor %}
  {% endif %}
  {% for collection in site.collections %}
    {% if collection.label != 'posts' %}
      {% for item in collection.docs %}
        {
          id: "{{ collection.label }}-{{ item.title | escape | strip | slugify }}",
          title: "{{ item.title | escape | strip | emojify | truncatewords: 13 }}",
          description: "{{ item.description | strip_html | strip_newlines | escape | strip }}",
          section: "{{ collection.label | capitalize }}",
          handler: () => {
            window.location.href = "{{ item.url | relative_url }}";
          },
        },
      {% endfor %}
    {% endif %}
  {% endfor %}
  {% if site.socials_in_search %}
    {% for social in site.data.socials %}
      {% assign social_id = "social-" | append: social[0] %}
      {% assign social_title = social[0] | capitalize %}
      {% capture social_url %}
        {% case social[0] %}
          {% when "email" %}mailto:{{ social[1] | encode_email }}
          {% when "twitter" %}https://twitter.com/{{ social[1] }}
          {% else %}{{ social[1] }}
        {% endcase %}
      {% endcapture %}
      {
        id: "{{ social_id }}",
        title: "{{ social_title }}",
        section: "Socials",
        handler: () => {
          window.open("{{ social_url | strip }}", "_blank");
        },
      },
    {% endfor %}
  {% endif %}
  {% if site.enable_darkmode %}
    {
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },
  {% endif %}
];
