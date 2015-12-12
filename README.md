# Config file

Default to `~/.config/rstblog-tools.conf`

Overridable with `RSTBLOG_TOOLS_CONFIG` environment variable

Content:

    BLOG_DIR=/path/to/blog
    BLOG_OUT_DIR=/path/to/blog/out
    BLOG_EDITOR=editor-to-start-when-creating-blog


# Tools

## rstblog-build

Generates the blog and serves it on localhost.

## rstblog-new

Asks a few questions and creates a new post in the `drafts` folder. Offers to
start editing the post with default editor.

## rstblog-publish

If the post is still in the `drafts` folder, make it public, set the `pub_date`
and move it to the proper blog post folder.

If the post is already public, update the `pub_date` to now. This is useful to
produce accurate dates in feeds so that the new post appears on top when an
agregator fetches it.

## rstblog-edit

List available posts and start editing the post with default editor.

## rstblog-deploy

Sync build output with blog out dir, commit and push the changes.
