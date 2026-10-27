# Setup — luislutchii GitHub profile

1. Copy this package into the root of the public repository `luislutchii/luislutchii`.
2. Install dependencies: `python -m pip install -r scripts/requirements.txt`.
3. Generate the portrait with your own photo:
   `python scripts/prep_photo.py path/to/your-photo.jpg`
   `python scripts/make_ascii_svg.py`
4. Generate the information card: `python scripts/make_info_card.py`.
5. Generate the real contribution graph:
   `python scripts/fetch_contributions.py`
   `python scripts/render_heatmap_svg.py`
6. Push to GitHub, then open **Actions → Update profile art → Run workflow** to test.

This package does not include your photo because no portrait was attached to this request. Until you run the portrait scripts, `lutchi-ascii.svg` is a placeholder. The contribution graph is also a placeholder until real data is fetched.

The scraper uses GitHub's public HTML without a personal access token. If GitHub changes its markup or blocks the request, the script stops instead of inventing data. The daily workflow updates only the heatmap; rerun the portrait/card scripts locally when your details change.
