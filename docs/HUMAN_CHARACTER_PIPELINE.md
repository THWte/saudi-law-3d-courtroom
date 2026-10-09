# Human Character Pipeline v1
- Entry: /frontend/courtroom-viewer.html (serve over HTTP, not file://).
- Load a licensed .glb (<=50 MB) via browser file picker. No upload endpoint or persistence.
- Select judge/prosecutor/defense/witness; import, normalize height, inspect meshes, bones, morph targets and animations; play embedded named clips.
- Model realism is entirely dependent on external legally licensed assets. No model is bundled.
- This is a standalone prototype; it does not replace the existing CSS landing scene or integrate the Flask backend.
- Dependencies are fetched from esm.sh CDN; offline use requires locally vendored pinned packages and an approved build.
- Security: GLB is untrusted input. Size/type checks are basic only; sandbox and asset scanning are required for production. Do not load private case data in this public repository.
- Limitations: no lip sync, facial retargeting, sitting pose correction, real court uniform verification, or full character production pipeline.
- Next: use authorized model sources; local dependency build; test in browser; wire event bus to simulation engine after authorization.
