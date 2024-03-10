from matdeck.Functions import *
import sqlite3

gui_dark()

    
class Interface():
    def __init__(self, parent):
        self.gui(parent)
        
        def convertToBinaryData(self, imageLocation):
            with open(imageLocation, 'rb') as file:
                blobData = file.read()
            return blobData
            
        # Database 
        # Create a database or connect to one 
        self.conn = sqlite3.connect('driver_data.db')
        # Create a cursor
        c = self.conn.cursor()
        # Create the table 
        c.execute("CREATE TABLE IF NOT EXISTS ddata (frame TEXT, speed FLOAT, signal INTEGER, x INTEGER, y INTEGER, brake TEXT, image TEXT);")
        
        print("ddata Table is Created")
        
        # Insert test values into database 
        
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake, image) VALUES ('5870','7.58','1','608', '659', 'applied', 'img_left_rect_color_5870.jpeg')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake, image) VALUES ('5871','7.25','1','1226', '660', 'applied', 'img_left_rect_color_5871.jpeg')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake, image) VALUES ('5872','6.69','1','1679', '513', 'applied', 'img_left_rect_color_5872.jpeg')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake, image) VALUES ('5873','6.47','1','1684', '537', 'applied', 'img_left_rect_color_5873.jpeg')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake, image) VALUES ('5946','23.97','0','8', '703', 'not_applied', 'img_left_rect_color_5946.jpeg')")
        
        
        # Commit changes 
        self.conn.commit()
        
        tableData=("SELECT * FROM ddata")
        c.execute(tableData) 
        self.records = c.fetchall()
        self.counter = 0

    def gui(self, parent):
        self.w1 = widget_from_settings(parent, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' nodeType='580' guiFC='0' x='0' guiBackColor='#ffffff' guiToolTip='' font='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' eventFunctionName='' guiBCC='1' isFrame='0' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' tooltip='' y='0' visible='1' variableName='w1' guiEnabled='1' width='500' height='450' m_editable='0' title='' guiFCC='0' guiFontColor='#c0c0c0' layout=''/></Widget>")
        self.frame1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' nodeType='580' guiFC='0' x='20' guiBackColor='#ffffff' guiToolTip='' m_frameColor='#000000' font='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' eventFunctionName='' guiBCC='1' isFrame='1' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' tooltip='' y='20' visible='1' variableName='frame1' guiEnabled='1' width='130' height='60' m_frameThickness='4' m_editable='0' title='' guiFCC='0' guiFontColor='#c0c0c0' layout=''/></Widget>")
        self.label2 = widget_from_settings(self.frame1, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' nodeType='593' guiFC='1' x='20' guiBackColor='#414141' guiToolTip='' font='Arial,30,-1,5,75,0,0,0,0,0' guiBCC='0' guiFont='Arial,30,-1,5,75,0,0,0,0,0' tooltip='' y='10' visible='1' variableName='label2' guiEnabled='1' width='90' height='42' m_editable='0' guiFCC='1' value='' guiFontColor='#080808'/></Widget>")
        set_widget_layout(self.frame1, "")
        self.image1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' m_backColor='#d4d4d4' nodeType='869' guiFC='0' x='15' guiBackColor='#d4d4d4' guiToolTip='' eventFunctionName='' guiBCC='1' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' tooltip='' y='90' visible='1' variableName='image1' guiEnabled='1' width='470' height='264' m_editable='0' guiFCC='0' guiFontColor='#c0c0c0'/></Widget>")
        self.indicator1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _tagName='' x='360' _showGenerator='0' _stepFrequency='5' _outChannelName='' _noUnitLable='1' guiFC='0' _wholeDigits='3' _showSwitch='0' _buttonColor='#595959' _titleBackgroundColor='#000000' _switchColor='#000000' _unit='' _scaleColor='#ffffff' _needleColor='#ed1c24' _channelOffsetExponent='0' _titleColor='#a0a0a4' _genMax='100' _frameColor='#282828' _blinkingTime='50' _frameImageIndex='0' guiFontColor='#c0c0c0' _showIndicator='1' _channelMultiplyExponent='0' _needleHeight='67' _minimum='0' _valueStartPosition='90' _lineWidth='4' _value='0' _decimalPlaces='0' guiToolTip='' _radialScaleEndAngle='180' _criticalEnd='100' _name='' _showTitle='0' _scaleLeft='0' _showNeedle='0' _showDigitmeter='0' _showTankBackground='1' _mainStepHeight='5' _valueStep='20' _stepWidth='1' tooltip='' _genConst='0' _scaleRadiusRatio='-1.9001363448404174e+305' _switchFontSize='13.5' _backgroundColor='#282828' _showCritical='1' height='60' _channelId='-1' _textColor='#ffffff' _genMin='-100' _showScale='0' _positionsNumber='1' _width='60' guiBCC='0' guiBackColor='#414141' _scaleHeight='60' _radius='-2.2305946220701992e+305' _mainStepFrequency='20' _criticalColor='#ff0000' _showCautionArea='1' _titleBackgroundTransparent='1' guiEnabled='1' _scaleType='2' _switchAutoFontSize='1' guiCursor='arrow' _state='0' width='60' _mainStepWidth='2' _measureScaleType='0' guiFCC='0' _scalePosition='0' _textSize='8' _noOutChannel='0' _needleWidth='3' visible='1' _startCautionArea='50' _buttonImageIndex='0' _typeIndex='0' _startCriticalArea='75' _textRaidus='67' y='20' nodeType='1054' _startValue='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _radialScaleRadius='67' m_editable='0' _needleType='2' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _showCriticalArea='1' _variableName='' _showTank='0' _title='Title' _endValue='100' _cautionColor='#808000' _offColor='#3d3d3d' _mode='3' _genType='1' _digitmeterColor='#ffffff' _criticalStart='85' _showFrame='0' _maximum='100' variableName='indicator1' _radialScaleBeginingAngle='-90' _blinking='0' _genRate='100' _switchType='0' _thermometerColor='#282828' _position='-90' _showBackground='0' _refreshInterval='50' _onColor='#5555fa' _thickness='2' _showThermometer='0' _stepHeight='2' eventFunctionName='' _showValues='1' _valueColor='#ffffff' _liquidColor='#d40000' _buttonSize='10' _blinkingColor='#5555fa' _channelMultiply='1' _needleIndex='0' _scaleTop='0' _scaleDistance='0' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _height='60' _tankColor='#000000' _valueEndPosition='-2.1204418629936053e+305' _valueTextSize='8' _scaleWidth='60' _takeUnitFromChannel='0' _lineStep='5' _showMeasureScale='0' _showSlider='0' _channelOffset='0'/></Widget>")
        self.digitmeter1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _tagName='' x='180' _showGenerator='0' _stepFrequency='5' _outChannelName='' _noUnitLable='1' guiFC='0' _wholeDigits='2' _showSwitch='0' _buttonColor='#595959' _titleBackgroundColor='#000000' _switchColor='#000000' _unit='' _scaleColor='#ffffff' _needleColor='#ed1c24' _channelOffsetExponent='0' _titleColor='#a0a0a4' _genMax='100' _frameColor='#282828' _blinkingTime='50' _frameImageIndex='0' guiFontColor='#c0c0c0' _showIndicator='0' _channelMultiplyExponent='0' _needleHeight='67' _minimum='0' _valueStartPosition='90' _lineWidth='4' _value='0' _decimalPlaces='2' guiToolTip='' _radialScaleEndAngle='180' _criticalEnd='100' _name='' _showTitle='0' _scaleLeft='0' _showNeedle='0' _showDigitmeter='1' _showTankBackground='1' _mainStepHeight='5' _valueStep='20' _stepWidth='1' tooltip='' _genConst='0' _scaleRadiusRatio='258.99079999999998' _switchFontSize='13.5' _backgroundColor='#282828' _showCritical='1' height='58' _channelId='-1' _textColor='#ffffff' _genMin='-100' _showScale='0' _positionsNumber='1' _width='145' guiBCC='0' guiBackColor='#414141' _scaleHeight='58' _radius='131.77999999999997' _mainStepFrequency='20' _criticalColor='#ff0000' _showCautionArea='1' _titleBackgroundTransparent='1' guiEnabled='1' _scaleType='2' _switchAutoFontSize='1' guiCursor='arrow' _state='0' width='145' _mainStepWidth='2' _measureScaleType='0' guiFCC='0' _scalePosition='0' _textSize='8' _noOutChannel='0' _needleWidth='3' visible='1' _startCautionArea='50' _buttonImageIndex='0' _typeIndex='0' _startCriticalArea='75' _textRaidus='67' y='20' nodeType='1054' _startValue='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _radialScaleRadius='67' m_editable='0' _needleType='2' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _showCriticalArea='1' _variableName='' _showTank='0' _title='Title' _endValue='100' _cautionColor='#808000' _offColor='#000000' _mode='6' _genType='1' _digitmeterColor='#ffffff' _criticalStart='85' _showFrame='1' _maximum='100' variableName='digitmeter1' _radialScaleBeginingAngle='-90' _blinking='0' _genRate='100' _switchType='0' _thermometerColor='#282828' _position='-90' _showBackground='1' _refreshInterval='50' _onColor='#000000' _thickness='2' _showThermometer='0' _stepHeight='2' eventFunctionName='' _showValues='1' _valueColor='#ffffff' _liquidColor='#d40000' _buttonSize='10' _blinkingColor='#000000' _channelMultiply='1' _needleIndex='0' _scaleTop='0' _scaleDistance='0' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _height='58' _tankColor='#000000' _valueEndPosition='76.532499999999999' _valueTextSize='8' _scaleWidth='145' _takeUnitFromChannel='0' _lineStep='5' _showMeasureScale='0' _showSlider='0' _channelOffset='0'/></Widget>")
        self.analog_edge1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _tagName='' x='180' _showGenerator='0' _stepFrequency='5' _outChannelName='' _noUnitLable='1' guiFC='0' _wholeDigits='3' _showSwitch='0' _buttonColor='#595959' _titleBackgroundColor='#000000' _switchColor='#000000' _unit='' _scaleColor='#ffffff' _needleColor='#ed1c24' _channelOffsetExponent='0' _titleColor='#a0a0a4' _genMax='100' _frameColor='#282828' _blinkingTime='50' _frameImageIndex='0' guiFontColor='#c0c0c0' _showIndicator='0' _channelMultiplyExponent='0' _needleHeight='46' _minimum='0' _valueStartPosition='135' _lineWidth='4' _value='0' _decimalPlaces='0' guiToolTip='' _radialScaleEndAngle='45' _criticalEnd='50' _name='' _showTitle='0' _scaleLeft='0' _showNeedle='1' _showDigitmeter='0' _showTankBackground='1' _mainStepHeight='5' _valueStep='20' _stepWidth='1' tooltip='' _genConst='0' _scaleRadiusRatio='0' _switchFontSize='13.5' _backgroundColor='#282828' _showCritical='1' height='72' _channelId='-1' _textColor='#ffffff' _genMin='-100' _showScale='1' _positionsNumber='1' _width='145' guiBCC='0' guiBackColor='#414141' _scaleHeight='255' _radius='0' _mainStepFrequency='15' _criticalColor='#ff0000' _showCautionArea='1' _titleBackgroundTransparent='1' guiEnabled='1' _scaleType='2' _switchAutoFontSize='1' guiCursor='arrow' _state='0' width='145' _mainStepWidth='1' _measureScaleType='0' guiFCC='0' _scalePosition='1' _textSize='8' _noOutChannel='0' _needleWidth='3' visible='1' _startCautionArea='50' _buttonImageIndex='0' _typeIndex='0' _startCriticalArea='75' _textRaidus='46' y='367' nodeType='1054' _startValue='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _radialScaleRadius='46' m_editable='0' _needleType='2' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _showCriticalArea='1' _variableName='' _showTank='0' _title='Title' _endValue='100' _cautionColor='#808000' _offColor='#000000' _mode='12' _genType='1' _digitmeterColor='#ffffff' _criticalStart='50' _showFrame='1' _maximum='60' variableName='analog_edge1' _radialScaleBeginingAngle='-45' _blinking='0' _genRate='100' _switchType='0' _thermometerColor='#282828' _position='-45' _showBackground='1' _refreshInterval='50' _onColor='#000000' _thickness='2' _showThermometer='0' _stepHeight='2' eventFunctionName='' _showValues='1' _valueColor='#ffffff' _liquidColor='#d40000' _buttonSize='7' _blinkingColor='#000000' _channelMultiply='1' _needleIndex='0' _scaleTop='0' _scaleDistance='0' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _height='72' _tankColor='#000000' _valueEndPosition='0' _valueTextSize='8' _scaleWidth='200' _takeUnitFromChannel='0' _lineStep='5' _showMeasureScale='0' _showSlider='0' _channelOffset='0'/></Widget>")
        self.button1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' nodeType='581' guiFC='1' x='30' guiBackColor='#414141' guiToolTip='' text='Previous' eventFunctionName='on_previous' guiBCC='0' guiFont='Arial,11,-1,5,75,0,0,0,0,0' y='390' visible='1' variableName='button1' guiEnabled='1' width='130' height='32' guiFCC='1' guiFontColor='#ffffff'/></Widget>")
        on_event(self.button1, self.on_previous)
        self.button2 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings guiCursor='arrow' nodeType='581' guiFC='1' x='340' guiBackColor='#414141' guiToolTip='' text='Next' eventFunctionName='on_next' guiBCC='0' guiFont='Arial,11,-1,5,75,0,0,0,0,0' y='390' visible='1' variableName='button2' guiEnabled='1' width='130' height='32' guiFCC='1' guiFontColor='#ffffff'/></Widget>")
        on_event(self.button2, self.on_next)
        self.indicator2 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _tagName='' x='420' _showGenerator='0' _stepFrequency='5' _outChannelName='' _noUnitLable='1' guiFC='0' _wholeDigits='3' _showSwitch='0' _buttonColor='#595959' _titleBackgroundColor='#000000' _switchColor='#000000' _unit='' _scaleColor='#ffffff' _needleColor='#ed1c24' _channelOffsetExponent='0' _titleColor='#a0a0a4' _genMax='100' _frameColor='#282828' _blinkingTime='50' _frameImageIndex='2' guiFontColor='#c0c0c0' _showIndicator='1' _channelMultiplyExponent='0' _needleHeight='67' _minimum='0' _valueStartPosition='90' _lineWidth='4' _value='0' _decimalPlaces='0' guiToolTip='' _radialScaleEndAngle='180' _criticalEnd='100' _name='' _showTitle='0' _scaleLeft='0' _showNeedle='0' _showDigitmeter='0' _showTankBackground='1' _mainStepHeight='5' _valueStep='20' _stepWidth='1' tooltip='' _genConst='0' _scaleRadiusRatio='3.2264148147010952e-307' _switchFontSize='13.5' _backgroundColor='#282828' _showCritical='1' height='60' _channelId='-1' _textColor='#ffffff' _genMin='-100' _showScale='0' _positionsNumber='1' _width='60' guiBCC='0' guiBackColor='#414141' _scaleHeight='60' _radius='1.3907195436668205e-307' _mainStepFrequency='20' _criticalColor='#ff0000' _showCautionArea='1' _titleBackgroundTransparent='1' guiEnabled='1' _scaleType='2' _switchAutoFontSize='1' guiCursor='arrow' _state='0' width='60' _mainStepWidth='2' _measureScaleType='0' guiFCC='0' _scalePosition='0' _textSize='8' _noOutChannel='0' _needleWidth='3' visible='1' _startCautionArea='50' _buttonImageIndex='0' _typeIndex='0' _startCriticalArea='75' _textRaidus='67' y='20' nodeType='1054' _startValue='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _radialScaleRadius='67' m_editable='0' _needleType='2' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _showCriticalArea='1' _variableName='' _showTank='0' _title='Title' _endValue='100' _cautionColor='#808000' _offColor='#3d3d3d' _mode='3' _genType='1' _digitmeterColor='#ffffff' _criticalStart='85' _showFrame='0' _maximum='100' variableName='indicator2' _radialScaleBeginingAngle='-90' _blinking='0' _genRate='100' _switchType='0' _thermometerColor='#282828' _position='-90' _showBackground='0' _refreshInterval='50' _onColor='#5555fa' _thickness='2' _showThermometer='0' _stepHeight='2' eventFunctionName='' _showValues='1' _valueColor='#ffffff' _liquidColor='#d40000' _buttonSize='10' _blinkingColor='#5555fa' _channelMultiply='1' _needleIndex='0' _scaleTop='0' _scaleDistance='0' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _height='60' _tankColor='#000000' _valueEndPosition='7.7879834400203193e-308' _valueTextSize='8' _scaleWidth='60' _takeUnitFromChannel='0' _lineStep='5' _showMeasureScale='0' _showSlider='0' _channelOffset='0'/></Widget>")
        set_widget_layout(self.w1, "")

    def on_next(self):      
        set_widget_value(self.label2,self.records[self.counter][0])
        set_widget_value(self.analog_edge1,self.records[self.counter][1])
        set_widget_value(self.indicator1,self.records[self.counter][2])
        set_widget_value(self.digitmeter1,self.records[self.counter][1])
        print(widget_value(self.label2))
        print(widget_value(self.analog_edge1))
        print(widget_value(self.digitmeter1))
        print(widget_value(self.indicator1))
        self.counter += 1
        # Close connection
        # conn.close()

    def on_previous(self):
        self.counter -= 1
        set_widget_value(self.label2,self.records[self.counter][0])
        set_widget_value(self.analog_edge1,self.records[self.counter][1])
        set_widget_value(self.indicator1,self.records[self.counter][2])
        set_widget_value(self.digitmeter1,self.records[self.counter][1])
        print(self.image1.value)
        print(widget_value(self.label2))
        print(widget_value(self.analog_edge1))
        print(widget_value(self.digitmeter1))
        print(widget_value(self.indicator1))
        
        


        
if __name__ == '__main__':
    a = Interface(0)
    show(a.w1)
    gui_loop()
    
    
