# -*- coding: utf-8 -*-
from typing import Any
from odoo import http
from odoo.http import request

class WebsiteSualasoft(http.Controller):
    @http.route('/homepage', type='http', auth='public', website=True, priority=20)
    def home(self, **kw):
        return request.render('website_sualasoft.sualasoft_homepage')

    @http.route('/services', type='http', auth='public', website=True, priority=20)
    def services(self, **kw):
        return request.render('website_sualasoft.sualasoft_services')

    @http.route('/contact', type='http', auth='public', website=True, priority=20)
    def contact(self, **kw):
        return request.render('website_sualasoft.sualasoft_contact')

    @http.route('/contact/submit', type='http', auth='public', website=True, methods=['POST'], priority=20)
    def contact_submit(self, **post):
        Contact = request.env['sualasoft.contact']
        
        try:
            Contact.create({
                'first_name': post.get('first_name', ''),
                'last_name': post.get('last_name', ''),
                'email': post.get('email', ''),
                'phone': post.get('phone', ''),
                'message': post.get('message', ''),
                'project_type': post.get('project_type', 'other'),
            })
            return request.render('website_sualasoft.contact_form_success')
        except Exception as e:
            return request.render('website_sualasoft.sualasoft_contact', {
                'error': 'Une erreur s\'est produite lors de l\'envoi du formulaire. Veuillez réessayer.'
            })

    @http.route('/references', type='http', auth='public', website=True, priority=20)
    def references(self, service_id=None, **kw):
        Reference = request.env['sualasoft.reference']
        Service = request.env['sualasoft.service']
        
        domain: list[tuple[str, str, Any]] = [('active', '=', True)]
        if service_id:
            try:
                service_id = int(service_id)
                domain.append(('service_ids', 'in', [service_id]))
            except (ValueError, TypeError):
                pass
        
        references = Reference.search(domain, order='sequence, name')
        services = Service.search([])
        
        values = {
            'references': references,
            'services': services,
        }
        return request.render('website_sualasoft.sualasoft_references_page', values)

    @http.route('/legal', type='http', auth='public', website=True, priority=20)
    def legal_notices(self, **kw):
        return request.render('website_sualasoft.sualasoft_legal_notices')

    @http.route('/privacy', type='http', auth='public', website=True, priority=20)
    def privacy_policy(self, **kw):
        return request.render('website_sualasoft.sualasoft_privacy_policy')

    @http.route('/blog', type='http', auth='public', website=True, priority=20)
    def blog(self, category_id=None, tag=None, **kw):
        BlogPost = request.env['blog.post']
        BlogCategory = request.env['blog.category']
        
        domain: list[tuple[str, str, Any]] = [('active', '=', True)]
        if category_id:
            try:
                category_id = int(category_id)
                domain.append(('category_ids', 'in', [category_id]))
            except (ValueError, TypeError):
                pass
        
        if tag:
            tag = tag.lower().strip()
            domain.append(('tags', 'ilike', tag))
        
        posts = BlogPost.search(domain, order='publication_date desc')
        categories = BlogCategory.search([('active', '=', True)], order='name')
        featured_posts = BlogPost.search([('active', '=', True), ('featured', '=', True)], 
                                         order='publication_date desc', limit=3)
        
        values = {
            'posts': posts,
            'categories': categories,
            'featured_posts': featured_posts,
            'selected_category_id': category_id,
            'selected_tag': tag,
        }
        return request.render('website_sualasoft.blog_posts_page', values)

    @http.route('/blog/<string:slug>', type='http', auth='public', website=True, priority=20)
    def blog_post(self, slug, **kw):
        BlogPost = request.env['blog.post']
        
        post = BlogPost.search([('slug', '=', slug), ('active', '=', True)], limit=1)
        if not post:
            return request.not_found()
        
        related_posts = BlogPost.search(
            [('active', '=', True), ('id', '!=', post.id), ('category_ids', 'in', post.category_ids.ids)],
            order='publication_date desc',
            limit=3
        )
        
        values = {
            'post': post,
            'related_posts': related_posts,
        }
        return request.render('website_sualasoft.blog_post_page', values)
