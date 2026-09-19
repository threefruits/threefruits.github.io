This is the source code to Anxing Xiao's public academic website: https://anxingxiao.com/.


## Styles

Pages load the prebuilt `styles/tailwind.css` followed by `styles/globals.css`.
GitHub Pages serves these files directly; no server-side build is needed.

After adding or changing Tailwind classes in HTML or inline JavaScript, rebuild:

```sh
npm ci
npm run build:css
```

Commit the generated `styles/tailwind.css` together with the HTML changes.
Edit `styles/globals.css` for custom styles; do not edit the generated CSS directly.
