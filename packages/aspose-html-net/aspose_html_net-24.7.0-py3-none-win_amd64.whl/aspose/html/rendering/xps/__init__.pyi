from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.html
import aspose.html.accessibility
import aspose.html.accessibility.results
import aspose.html.accessibility.saving
import aspose.html.collections
import aspose.html.converters
import aspose.html.diagnostics
import aspose.html.dom
import aspose.html.dom.attributes
import aspose.html.dom.canvas
import aspose.html.dom.css
import aspose.html.dom.events
import aspose.html.dom.mutations
import aspose.html.dom.svg
import aspose.html.dom.svg.datatypes
import aspose.html.dom.svg.events
import aspose.html.dom.svg.filters
import aspose.html.dom.svg.paths
import aspose.html.dom.svg.saving
import aspose.html.dom.traversal
import aspose.html.dom.traversal.filters
import aspose.html.dom.views
import aspose.html.dom.xpath
import aspose.html.drawing
import aspose.html.forms
import aspose.html.io
import aspose.html.loading
import aspose.html.net
import aspose.html.net.headers
import aspose.html.net.messagefilters
import aspose.html.net.messagehandlers
import aspose.html.rendering
import aspose.html.rendering.doc
import aspose.html.rendering.fonts
import aspose.html.rendering.image
import aspose.html.rendering.pdf
import aspose.html.rendering.pdf.encryption
import aspose.html.rendering.xps
import aspose.html.saving
import aspose.html.saving.resourcehandlers
import aspose.html.services
import aspose.html.toolkit
import aspose.html.toolkit.markdown
import aspose.html.toolkit.markdown.syntax
import aspose.html.toolkit.markdown.syntax.extensions
import aspose.html.toolkit.markdown.syntax.parser
import aspose.html.toolkit.markdown.syntax.parser.extensions
import aspose.html.toolkit.markdown.syntax.parser.extensions.gfm
import aspose.html.toolkit.markdown.syntax.text
import aspose.html.toolkit.optimizers
import aspose.html.window

class XpsDevice(aspose.html.rendering.Device):
    '''Represents rendering to a xps document.'''
    
    def restore_graphic_context(self):
        '''Restores the entire graphics context to its former value by popping it from the stack.'''
        ...
    
    def line_to(self, pt : aspose.pydrawing.PointF):
        '''Appends a straight line segment from the current point to the point (pt). The new current point is pt.
        
        :param pt: Point of where to create the line to.'''
        ...
    
    def move_to(self, pt : aspose.pydrawing.PointF):
        '''Begins a new subpath by moving the current point to coordinates of the parameter pt, omitting any connecting line segment.
        If the previous path construction method in the current path was also "MoveTo", the new "MoveTo" overrides it;
        no vestige of the previous "MoveTo" operation remains in the path.
        
        :param pt: Point of where to move the path to.'''
        ...
    
    def cubic_bezier_to(self, pt1 : aspose.pydrawing.PointF, pt2 : aspose.pydrawing.PointF, pt3 : aspose.pydrawing.PointF):
        '''Appends a cubic Bézier curve to the current path. The curve extends from the current point to the point pt2,
        using pt1 and pt2 as the Bézier control points. The new current point is pt3.
        
        :param pt1: Coordinates of first point
        :param pt2: Coordinates of second point
        :param pt3: Coordinates of third point'''
        ...
    
    def add_rect(self, rect : aspose.pydrawing.RectangleF):
        '''Appends a rectangle to the current path as a complete subpath.
        
        :param rect: A rectangle to draw.'''
        ...
    
    def close_path(self):
        '''Closes the current subpath by appending a straight line segment from the current point to the starting point of the subpath.
        If the current subpath is already closed, "ClosePath" does nothing.
        This operator terminates the current subpath. Appending another segment to the current path begins a new subpath,
        even if the new segment begins at the endpoint reached by the "ClosePath" method.'''
        ...
    
    def clip(self, mode : aspose.pydrawing.drawing2d.FillMode):
        '''Modifies the current clipping path by intersecting it with the current path, using the FillMode rule to determine the region to fill.
        This method terminates current path.
        
        :param mode: Filling mode specifies how the interior of a closed path is clipped'''
        ...
    
    def fill(self, mode : aspose.pydrawing.drawing2d.FillMode):
        '''Fills the entire region enclosed by the current path.
        If the path consists of several disconnected subpaths, it fills the insides of all subpaths,
        considered together.
        This method terminates current path.
        
        :param mode: Filling mode specifies how the interior of a closed path is filled'''
        ...
    
    def stroke_and_fill(self, mode : aspose.pydrawing.drawing2d.FillMode):
        '''Strokes and fill current path.
        This method terminates current path.
        
        :param mode: Filling mode specifies how the interior of a closed path is filled.'''
        ...
    
    def stroke(self):
        '''Strokes a line along the current path. The stroked line follows each straight or curved segment in the path,
        centered on the segment with sides parallel to it. Each of the path’s subpaths is treated separately.
        This method terminates current path.'''
        ...
    
    def fill_text(self, text : str, pt : aspose.pydrawing.PointF):
        '''Fills the specified text string at the specified location.
        
        :param text: String to fill.
        :param pt: Point that specifies the coordinates of the text.'''
        ...
    
    def stroke_text(self, text : str, pt : aspose.pydrawing.PointF):
        '''Strokes the specified text string at the specified location.
        
        :param text: String to stroke.
        :param pt: Point that specifies the coordinates where to start the text.'''
        ...
    
    def begin_document(self, document : aspose.html.dom.Document):
        '''Begins rendering of the document.
        
        :param document: The document.'''
        ...
    
    def begin_element(self, element : aspose.html.dom.Element, rect : aspose.pydrawing.RectangleF) -> bool:
        '''Begins rendering of the element.
        
        :param element: The :py:class:`aspose.html.dom.Element`.
        :param rect: Bounding box of the node.
        :returns: Returns [true] if element should be processed.'''
        ...
    
    def begin_page(self, size : aspose.pydrawing.SizeF):
        '''Begins rendering of the new page.
        
        :param size: Size of the page.'''
        ...
    
    def end_page(self):
        '''Ends rendering of the current page.'''
        ...
    
    def flush(self):
        '''Flushes all data to output stream.'''
        ...
    
    def end_element(self, element : aspose.html.dom.Element):
        '''Ends rendering of the element.
        
        :param element: The :py:class:`aspose.html.dom.Element`.'''
        ...
    
    def draw_image(self, data : bytes, type : aspose.html.rendering.ImageType, rect : aspose.pydrawing.RectangleF):
        '''Draws the specified image.
        
        :param data: An array of bytes representing the image.
        :param type: Image type.
        :param rect: A rectangel which determines position and size to draw.'''
        ...
    
    def save_graphic_context(self):
        ...
    
    def end_document(self):
        ...
    
    @property
    def options(self) -> aspose.html.rendering.xps.XpsRenderingOptions:
        ...
    
    @property
    def graphic_context(self) -> XpsDevice.XpsGraphicContext:
        ...
    
    ...

class XpsRenderingOptions(aspose.html.rendering.RenderingOptions):
    '''Represents rendering options for :py:class:`aspose.html.rendering.xps.XpsDevice`.'''
    
    @property
    def css(self) -> aspose.html.rendering.CssOptions:
        '''Gets a :py:class:`aspose.html.rendering.CssOptions` object which is used for configuration of css properties processing.'''
        ...
    
    @property
    def page_setup(self) -> aspose.html.rendering.PageSetup:
        ...
    
    @property
    def horizontal_resolution(self) -> aspose.html.drawing.Resolution:
        ...
    
    @horizontal_resolution.setter
    def horizontal_resolution(self, value : aspose.html.drawing.Resolution):
        ...
    
    @property
    def background_color(self) -> aspose.pydrawing.Color:
        ...
    
    @background_color.setter
    def background_color(self, value : aspose.pydrawing.Color):
        ...
    
    @property
    def vertical_resolution(self) -> aspose.html.drawing.Resolution:
        ...
    
    @vertical_resolution.setter
    def vertical_resolution(self, value : aspose.html.drawing.Resolution):
        ...
    
    ...

