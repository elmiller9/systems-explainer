# sources/

Raw analyses the playbook is distilled from: video breakdowns, transcripts and research notes. `update-playbook` saves new ones here.

Everything in this folder except this README is git-ignored, because it can contain third-party transcripts or private material. The playbook keeps only the patterns, written in original wording, so the plugin works without these files. Back them up separately if you want to keep them.

## Analysis prompt

The prompt used to produce the original analyses (with Google AI Studio). Swap in the video URL:

```
Analyze this video as a production template. <URL>

Give me:
1.  Full transcript with timestamps.
2.  Scene-by-scene breakdown: what's on screen, camera/screen-recording style, transitions, on-screen text, callouts, and zooms.
3.  Granular Keyframe Blueprints: Act as an art director and provide a granular, pixel-level descriptive breakdown of the most important keyframes. Detail the exact layout, spatial relationships, UI element shapes (e.g., flat, rounded corners, drop shadows), character/avatar placement, typography usage (headers vs. body text), and precise color mapping so a UI or motion designer could recreate these frames exactly.
4.  Pacing: length of each segment, and exactly how the hook works in the first 5 seconds.
5.  Narration style: tone, point of view, and any recurring rhetorical phrases or script structures.
6.  Global Visual Style: overall master color palette, font styles, diagram types, tools shown, and the general aesthetic rules (e.g., "retro blueprint" or "neon cyberpunk").
7.  The repeatable formula: a step-by-step framework to recreate the logic and flow of the video for my own content.
```
