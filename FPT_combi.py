# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FPT_MainWin
###########################################################################

class FPT_MainWin ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Footprint Terminator_combi_v04", pos = wx.DefaultPosition, size = wx.Size( 526,601 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,600 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		file_format = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"File Format: IL XL Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		
		file_format.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer1.Add( file_format, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		ImportZone = wx.BoxSizer( wx.VERTICAL )
		
		import_interface = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Import File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		import_interface.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_filePicker.SetMinSize( wx.Size( 300,-1 ) )
		
		import_interface.Add( self.m_filePicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		ImportZone.Add( import_interface, 1, wx.EXPAND, 5 )
		
		import_params = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Lines to skip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		import_params.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_rowstoskip = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_rowstoskip.SetMinSize( wx.Size( 30,-1 ) )
		self.m_rowstoskip.SetMaxSize( wx.Size( 30,-1 ) )
		
		import_params.Add( self.m_rowstoskip, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"InLine column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		import_params.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_il_col = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_il_col.SetMinSize( wx.Size( 30,-1 ) )
		self.m_il_col.SetMaxSize( wx.Size( 30,-1 ) )
		
		import_params.Add( self.m_il_col, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"XLine column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		import_params.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_xl_col = wx.TextCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_xl_col.SetMinSize( wx.Size( 30,-1 ) )
		self.m_xl_col.SetMaxSize( wx.Size( 30,-1 ) )
		
		import_params.Add( self.m_xl_col, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Data column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		import_params.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_data_col = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_data_col.SetMinSize( wx.Size( 30,-1 ) )
		self.m_data_col.SetMaxSize( wx.Size( 30,-1 ) )
		
		import_params.Add( self.m_data_col, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		ImportZone.Add( import_params, 1, wx.EXPAND, 5 )
		
		Importbtn_zone = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		Importbtn_zone.Add( self.m_staticText6, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Import file", wx.DefaultPosition, wx.DefaultSize, 0 )
		Importbtn_zone.Add( self.m_button1, 8, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.t_imp_status = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_imp_status.Wrap( -1 )
		Importbtn_zone.Add( self.t_imp_status, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		ImportZone.Add( Importbtn_zone, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( ImportZone, 1, wx.EXPAND, 5 )
		
		inline_range = wx.BoxSizer( wx.HORIZONTAL )
		
		self.InLines_Min = wx.StaticText( self, wx.ID_ANY, u"InLines:  Min:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.InLines_Min.Wrap( -1 )
		inline_range.Add( self.InLines_Min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_il_min = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_il_min.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_il_min.SetMaxSize( wx.Size( 50,-1 ) )
		
		inline_range.Add( self.m_text_il_min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.Max = wx.StaticText( self, wx.ID_ANY, u"Max:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Max.Wrap( -1 )
		inline_range.Add( self.Max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_il_max = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_il_max.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_il_max.SetMaxSize( wx.Size( 50,-1 ) )
		
		inline_range.Add( self.m_text_il_max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBox_IL_rev = wx.CheckBox( self, wx.ID_ANY, u"Plot in reverse order", wx.DefaultPosition, wx.DefaultSize, 0 )
		inline_range.Add( self.m_checkBox_IL_rev, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( inline_range, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		xl_range1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.InLinesMin1 = wx.StaticText( self, wx.ID_ANY, u"XLines:   Min:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.InLinesMin1.Wrap( -1 )
		xl_range1.Add( self.InLinesMin1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_xl_min = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_xl_min.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_xl_min.SetMaxSize( wx.Size( 50,-1 ) )
		
		xl_range1.Add( self.m_text_xl_min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.Max1 = wx.StaticText( self, wx.ID_ANY, u"Max:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Max1.Wrap( -1 )
		xl_range1.Add( self.Max1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_xl_max = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_xl_max.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_xl_max.SetMaxSize( wx.Size( 50,-1 ) )
		
		xl_range1.Add( self.m_text_xl_max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBox_XL_rev = wx.CheckBox( self, wx.ID_ANY, u"Plot in reverse order", wx.DefaultPosition, wx.DefaultSize, 0 )
		xl_range1.Add( self.m_checkBox_XL_rev, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( xl_range1, 1, wx.EXPAND, 5 )
		
		asp = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"IL/XL aspect ratio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		asp.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_text_il_xl_aspect = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_il_xl_aspect.SetMinSize( wx.Size( 40,-1 ) )
		self.m_text_il_xl_aspect.SetMaxSize( wx.Size( 40,-1 ) )
		
		asp.Add( self.m_text_il_xl_aspect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( asp, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_checkBox_rad = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Radial preserving filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_rad.SetValue(True) 
		self.m_checkBox_rad.SetToolTipString( u"Защищает центр спектра" )
		
		sbSizer2.Add( self.m_checkBox_rad, 0, wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Radius:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer14.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textRad_rad = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textRad_rad.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textRad_rad.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14.Add( self.m_textRad_rad, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Aspect:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer14.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textRad_asp = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textRad_asp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textRad_asp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14.Add( self.m_textRad_asp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Smoothness:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer14.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textRad_sm = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textRad_sm.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textRad_sm.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14.Add( self.m_textRad_sm, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		self.m_staticText38.Hide()
		
		bSizer14.Add( self.m_staticText38, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textRad_kdamp = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textRad_kdamp.Enable( False )
		self.m_textRad_kdamp.Hide()
		self.m_textRad_kdamp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textRad_kdamp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14.Add( self.m_textRad_kdamp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_checkBox_gau1 = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Gaussian notch filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_gau1.SetValue(True) 
		sbSizer11.Add( self.m_checkBox_gau1, 0, wx.ALL, 5 )
		
		bSizer14111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16111 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"InLine coord:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16111.Wrap( -1 )
		bSizer14111.Add( self.m_staticText16111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textGauIL = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauIL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauIL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14111.Add( self.m_textGauIL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText17111 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17111.Wrap( -1 )
		bSizer14111.Add( self.m_staticText17111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauILSize = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauILSize.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauILSize.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14111.Add( self.m_textGauILSize, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText18111 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Length:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18111.Wrap( -1 )
		bSizer14111.Add( self.m_staticText18111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauILWid = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauILWid.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauILWid.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14111.Add( self.m_textGauILWid, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pow11 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pow11.Wrap( -1 )
		bSizer14111.Add( self.pow11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauIL_kdamp = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauIL_kdamp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauIL_kdamp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer14111.Add( self.m_textGauIL_kdamp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer14111, 1, wx.EXPAND, 5 )
		
		bSizer1412 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1612 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"XLine coord: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1612.Wrap( -1 )
		bSizer1412.Add( self.m_staticText1612, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textGauXL = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauXL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauXL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1412.Add( self.m_textGauXL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1712 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1712.Wrap( -1 )
		bSizer1412.Add( self.m_staticText1712, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauXLSize = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauXLSize.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauXLSize.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1412.Add( self.m_textGauXLSize, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1812 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Length:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1812.Wrap( -1 )
		bSizer1412.Add( self.m_staticText1812, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauXLWid = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauXLWid.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauXLWid.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1412.Add( self.m_textGauXLWid, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pow21 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pow21.Wrap( -1 )
		bSizer1412.Add( self.pow21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textGauXL_kdamp = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textGauXL_kdamp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_textGauXL_kdamp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1412.Add( self.m_textGauXL_kdamp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer1412, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_checkBox_rad_notch = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Radial notch filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_rad_notch.SetValue(True) 
		sbSizer1.Add( self.m_checkBox_rad_notch, 0, wx.ALL, 5 )
		
		bSizer1411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1611 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"il1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1611.Wrap( -1 )
		bSizer1411.Add( self.m_staticText1611, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_text_rad1IL = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_rad1IL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_rad1IL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1411.Add( self.m_text_rad1IL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"xl1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer1411.Add( self.m_staticText28, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_rad1XL = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_rad1XL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_rad1XL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1411.Add( self.m_text_rad1XL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1711 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1711.Wrap( -1 )
		bSizer1411.Add( self.m_staticText1711, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad1Size = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad1Size.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad1Size.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1411.Add( self.m_text_Rad1Size, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1811 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Aspect:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1811.Wrap( -1 )
		bSizer1411.Add( self.m_staticText1811, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad1Asp = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad1Asp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad1Asp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1411.Add( self.m_text_Rad1Asp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pow1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pow1.Wrap( -1 )
		bSizer1411.Add( self.pow1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad1kdamp = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad1kdamp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad1kdamp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer1411.Add( self.m_text_Rad1kdamp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer1411, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"il2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer141.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_text_rad2IL = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_rad2IL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_rad2IL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer141.Add( self.m_text_rad2IL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"xl2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer141.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_rad2XL = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_rad2XL.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_rad2XL.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer141.Add( self.m_text_rad2XL, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText171 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer141.Add( self.m_staticText171, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad2Size = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad2Size.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad2Size.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer141.Add( self.m_text_Rad2Size, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText181 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Aspect:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		bSizer141.Add( self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad2Asp = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad2Asp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad2Asp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer141.Add( self.m_text_Rad2Asp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pow2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pow2.Wrap( -1 )
		bSizer141.Add( self.pow2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_text_Rad2kdamp = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_Rad2kdamp.SetMinSize( wx.Size( 50,-1 ) )
		self.m_text_Rad2kdamp.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer141.Add( self.m_text_Rad2kdamp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		Importbtn_zone1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.t_plot_status = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_plot_status.Wrap( -1 )
		Importbtn_zone1.Add( self.t_plot_status, 10, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_btnPlot = wx.Button( self, wx.ID_ANY, u"Plot / Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		Importbtn_zone1.Add( self.m_btnPlot, 8, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		Importbtn_zone1.Add( self.m_staticText41, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button_export = wx.Button( self, wx.ID_ANY, u"Export to file", wx.DefaultPosition, wx.DefaultSize, 0 )
		Importbtn_zone1.Add( self.m_button_export, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( Importbtn_zone1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileOpen )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnImportPress )
		self.m_btnPlot.Bind( wx.EVT_BUTTON, self.OnPlotBtn )
		self.m_button_export.Bind( wx.EVT_BUTTON, self.ExportClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileOpen( self, event ):
		event.Skip()
	
	def OnImportPress( self, event ):
		event.Skip()
	
	def OnPlotBtn( self, event ):
		event.Skip()
	
	def ExportClicked( self, event ):
		event.Skip()
	

###########################################################################
## Class FramePlot
###########################################################################

class FramePlot ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Plot", pos = wx.Point( 20,20 ), size = wx.Size( 1500,1000 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onPlotClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onPlotClose( self, event ):
		event.Skip()
	

