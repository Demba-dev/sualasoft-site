from odoo import models, fields
import re
import unicodedata


def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip()
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


class BlogCategory(models.Model):
    _name = 'blog.category'
    _description = 'Blog Category'
    _order = 'name'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    slug = fields.Char(string='URL Slug', required=True, unique=True)
    color = fields.Integer(string='Color Index', default=1)
    post_ids = fields.Many2many(
        'blog.post',
        'blog_post_category_rel',
        'category_id',
        'post_id',
        string='Blog Posts'
    )

    active = fields.Boolean(default=True)

    def _compute_slug(self):
        for record in self:
            if not record.slug and record.name:
                record.slug = slugify(record.name)


class BlogPost(models.Model):
    _name = 'blog.post'
    _description = 'Blog Post'
    _order = 'publication_date desc, name'

    name = fields.Char(string='Title', required=True)
    slug = fields.Char(string='URL Slug', required=True, unique=True)
    content = fields.Html(string='Content', required=True)
    summary = fields.Text(string='Summary', help='Short excerpt displayed in listings')

    publication_date = fields.Datetime(
        string='Publication Date',
        default=fields.Datetime.now,
        required=True
    )

    author_id = fields.Many2one(
        'res.users',
        string='Author',
        default=lambda self: self.env.user,
        required=True
    )

    category_ids = fields.Many2many(
        'blog.category',
        'blog_post_category_rel',
        'post_id',
        'category_id',
        string='Categories'
    )

    tags = fields.Char(
        string='Tags',
        help='Comma-separated tags (ex: odoo, web, mobile)'
    )

    featured_image = fields.Image(string='Featured Image')
    featured = fields.Boolean(string='Featured Post', default=False)

    active = fields.Boolean(default=True)
    created_date = fields.Datetime(string='Date Created', default=fields.Datetime.now)
    updated_date = fields.Datetime(string='Last Updated', default=fields.Datetime.now)

    _sql_constraints = [
        ('slug_unique', 'unique(slug)', 'The slug must be unique'),
    ]

    def _compute_slug(self):
        for record in self:
            if not record.slug and record.name:
                record.slug = slugify(record.name)

    def action_toggle_featured(self):
        self.featured = not self.featured
        return True
