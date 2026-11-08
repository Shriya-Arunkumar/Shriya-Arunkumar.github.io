# Shriya Arunkumar — Portfolio

A responsive static portfolio covering robotics, computer vision, project work,
and research interests in human–robot interaction.

## Preview locally

From this directory:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000 in a browser. Stop the server with Ctrl+C.
No package installation or build step is needed.

## Files

- `index.html`: content, projects, research direction, bio, and contact links.
- `styles.css`: responsive layout, light/dark palettes, and restrained interaction styles.
- `script.js`: saved theme preference, mobile navigation, project filters, and active navigation.
- `pfp4.jpg`: retained original asset; it is no longer displayed on the site.

The original typography uses Bebas Neue, DM Sans, and Playfair Display from Google
Fonts, with local fallback fonts. Project thumbnail slots are reserved for
supplied YouTube thumbnails; no illustrative project graphics are displayed. Research topics describe interests
and ongoing project exploration; they are not publication or validation claims.

## Project pages

Each project title and thumbnail slot opens a dedicated static page under
`projects/`. These pages share the home page's fonts, colors, theme preference,
and navigation, and provide links back to the project list and to the next project.
The Trimodal Robot page intentionally contains only a public abstract, tools,
and an email contact, with no implementation details or source repository.
