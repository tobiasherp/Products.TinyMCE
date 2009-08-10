from zope.component import getUtility
from Products.TinyMCE.interfaces.utility import ITinyMCE
from Products.CMFCore.utils import getToolByName

def meta_types_to_portal_types(meta_types):
    """Convert meta types to portal types"""
    meta_types = meta_types.replace(u'ATTopic', u'Topic')
    meta_types = meta_types.replace(u'ATEvent', u'Event')
    meta_types = meta_types.replace(u'ATFile', u'File')
    meta_types = meta_types.replace(u'ATFolder', u'Folder')
    meta_types = meta_types.replace(u'ATImage', u'Image')
    meta_types = meta_types.replace(u'ATBTreeFolder', u'Large Plone Folder')
    meta_types = meta_types.replace(u'ATNewsItem', u'News Item')
    meta_types = meta_types.replace(u'ATDocument', u'Document')
    return meta_types

def upgrade_10_to_11(setuptool):
    """Upgrade TinyMCE from 1.0 to 1.1"""

    # http://plone.org/products/tinymce/issues/26
    tinymce = getUtility(ITinyMCE)
    tinymce.styles = tinymce.styles.replace(u'Pull-quote|div|pullquote', u'Pull-quote|blockquote|pullquote')

    # Add entity_encoding property
    tinymce.entity_encoding = u"raw"

    # Add custom toolbar buttons property
    tinymce.customtoolbarbuttons = u""

    # Add rooted property
    tinymce.rooted = False

    # Convert meta_types to portal_types
    tinymce.containsobjects = meta_types_to_portal_types(tinymce.containsobjects)
    tinymce.containsanchors = meta_types_to_portal_types(tinymce.containsanchors)
    tinymce.linkable = meta_types_to_portal_types(tinymce.linkable)
    tinymce.imageobjects = meta_types_to_portal_types(tinymce.imageobjects)

    # Unregister old js and register new js
    setuptool.runAllImportStepsFromProfile('profile-Products.TinyMCE:upgrade_10_to_11')
