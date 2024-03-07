from matdeck.Functions import *
import sqlite3
gui_dark()

    
class Interface():

    #for row in records:
        #print(row[0])
        #print(row[1])
        #print(row[2])
        #print(row[3])
        #print(row[4],"\n")
           
    def __init__(self, parent):
        self.gui(parent)
        # Database 
        # Create a database or connect to one 
        self.conn = sqlite3.connect('driver_data.db')
        # Create a cursor
        c = self.conn.cursor()
        # Create the table 
        c.execute("CREATE TABLE IF NOT EXISTS ddata (frame TEXT, speed FLOAT, signal INTEGER, x INTEGER, y INTEGER, brake TEXT);")
        
        print("ddata Table is Created")
        
        # Insert test values into database 
        
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake) VALUES ('5870','7.58','1','608', '659', 'applied')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake) VALUES ('5871','7.25','1','1226', '660', 'applied')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake) VALUES ('5872','6.69','1','1679', '513', 'applied')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake) VALUES ('5873','6.47','1','1684', '537', 'applied')")
        c.execute("INSERT INTO ddata (frame, speed, signal, x, y, brake) VALUES ('5946','23.97','0','8', '703', 'not_applied')")
        
        # Commit changes 
        self.conn.commit()
        
        tableData=("SELECT * FROM ddata")
        c.execute(tableData) 
        self.records = c.fetchall()
        self.counter = 0


    def gui(self, parent):
        self.w1 = widget_from_settings(parent, "<!DOCTYPE Widget><Widget><GuiSettings width='500' eventFunctionName='' guiBCC='1' nodeType='580' title='' x='0' guiEnabled='1' guiBackColor='#ffffff' layout='' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' guiFC='0' guiFontColor='#c0c0c0' guiToolTip='' guiFCC='0' y='0' variableName='w1' visible='1' font='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' tooltip='' guiCursor='arrow' isFrame='0' m_editable='0' height='450'/></Widget>")
        self.frame1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings width='120' eventFunctionName='' guiBCC='1' nodeType='580' title='' x='30' guiEnabled='1' guiBackColor='#c2d9d1' layout='' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' m_frameThickness='4' guiFC='0' guiFontColor='#c0c0c0' guiToolTip='' guiFCC='0' y='20' variableName='frame1' visible='1' font='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' m_frameColor='#949494' tooltip='' guiCursor='arrow' isFrame='1' m_editable='0' height='40'/></Widget>")
        self.label2 = widget_from_settings(self.frame1, "<!DOCTYPE Widget><Widget><GuiSettings width='100' guiBCC='0' nodeType='593' x='10' guiEnabled='1' guiBackColor='#414141' guiFont='Georgia,10,-1,5,50,0,0,0,0,0' value='Frame Number' guiFC='1' guiFontColor='#080808' guiToolTip='' guiFCC='1' y='10' variableName='label2' visible='1' font='Georgia,10,-1,5,50,0,0,0,0,0' tooltip='' guiCursor='arrow' m_editable='0' height='22'/></Widget>")
        set_widget_layout(self.frame1, "")
        self.image1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings width='480' eventFunctionName='' guiBCC='1' nodeType='869' x='10' guiEnabled='1' guiBackColor='#d4d4d4' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' m_backColor='#d4d4d4' guiFC='0' guiFontColor='#c0c0c0' guiToolTip='' guiFCC='0' y='80' variableName='image1' visible='1' tooltip='' guiCursor='arrow' m_editable='0' height='260'/></Widget>")
        self.indicator1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _startCautionArea='50' x='390' _unit='' _buttonImageIndex='0' _liquidColor='#d40000' _blinkingTime='50' _textSize='8' _channelId='-1' _typeIndex='0' _thermometerColor='#282828' _needleWidth='3' _channelMultiply='1' _needleHeight='67' guiCursor='arrow' height='60' _showSwitch='0' _genConst='0' _showCritical='1' _showCautionArea='1' _radialScaleEndAngle='180' _channelOffsetExponent='0' _height='60' _radialScaleRadius='67' _measureScaleType='0' _genMax='100' _scaleDistance='0' _switchAutoFontSize='1' _frameColor='#282828' _mode='3' _titleBackgroundColor='#000000' guiFontColor='#c0c0c0' _frameImageIndex='0' _switchType='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _showScale='0' _takeUnitFromChannel='0' _scaleRadiusRatio='-1.9001363448404174e+305' y='10' _thickness='2' _showCriticalArea='1' _backgroundColor='#282828' _criticalColor='#ff0000' _showFrame='0' _mainStepHeight='5' guiBackColor='#414141' _titleBackgroundTransparent='1' _channelOffset='0' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _title='Title' _needleIndex='0' m_editable='0' _valueEndPosition='-2.1204418629936053e+305' _buttonSize='10' variableName='indicator1' _showMeasureScale='0' _showGenerator='0' _scaleColor='#ffffff' guiFC='0' _showBackground='0' _lineStep='5' width='60' _minimum='0' _noOutChannel='0' visible='1' _wholeDigits='3' _radius='-2.2305946220701992e+305' eventFunctionName='' _name='' _valueStartPosition='90' _criticalEnd='100' _state='0' nodeType='1054' _showThermometer='0' guiFCC='0' _switchFontSize='13.5' _scalePosition='0' _outChannelName='' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _channelMultiplyExponent='0' _radialScaleBeginingAngle='-90' _tankColor='#000000' _position='-90' _maximum='100' _decimalPlaces='0' _showNeedle='0' _valueTextSize='8' _onColor='#5555fa' _showValues='1' _buttonColor='#595959' _showSlider='0' _value='0' _textRaidus='67' _offColor='#3d3d3d' _scaleLeft='0' _showDigitmeter='0' _genType='1' _startCriticalArea='75' _needleColor='#ed1c24' _genMin='-100' _criticalStart='85' _showIndicator='1' _stepHeight='2' _tagName='' _titleColor='#a0a0a4' _showTitle='0' _genRate='100' guiToolTip='' tooltip='' _blinking='0' _scaleTop='0' _valueStep='20' _lineWidth='4' _mainStepWidth='2' _cautionColor='#808000' _scaleHeight='60' _stepWidth='1' _mainStepFrequency='20' _width='60' _textColor='#ffffff' _scaleType='2' _needleType='2' _positionsNumber='1' guiBCC='0' _stepFrequency='5' _noUnitLable='1' _refreshInterval='50' _startValue='0' _variableName='' _scaleWidth='60' _switchColor='#000000' guiEnabled='1' _valueColor='#ffffff' _endValue='100' _blinkingColor='#5555fa' _digitmeterColor='#ffffff' _showTank='0' _showTankBackground='1'/></Widget>")
        self.digitmeter1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _startCautionArea='50' x='170' _unit='' _buttonImageIndex='0' _liquidColor='#d40000' _blinkingTime='50' _textSize='8' _channelId='-1' _typeIndex='0' _thermometerColor='#282828' _needleWidth='3' _channelMultiply='1' _needleHeight='67' guiCursor='arrow' height='58' _showSwitch='0' _genConst='0' _showCritical='1' _showCautionArea='1' _radialScaleEndAngle='180' _channelOffsetExponent='0' _height='58' _radialScaleRadius='67' _measureScaleType='0' _genMax='100' _scaleDistance='0' _switchAutoFontSize='1' _frameColor='#282828' _mode='6' _titleBackgroundColor='#000000' guiFontColor='#c0c0c0' _frameImageIndex='0' _switchType='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _showScale='0' _takeUnitFromChannel='0' _scaleRadiusRatio='258.99079999999998' y='10' _thickness='2' _showCriticalArea='1' _backgroundColor='#282828' _criticalColor='#ff0000' _showFrame='1' _mainStepHeight='5' guiBackColor='#414141' _titleBackgroundTransparent='1' _channelOffset='0' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _title='Title' _needleIndex='0' m_editable='0' _valueEndPosition='76.532499999999999' _buttonSize='10' variableName='digitmeter1' _showMeasureScale='0' _showGenerator='0' _scaleColor='#ffffff' guiFC='0' _showBackground='1' _lineStep='5' width='170' _minimum='0' _noOutChannel='0' visible='1' _wholeDigits='3' _radius='131.77999999999997' eventFunctionName='' _name='' _valueStartPosition='90' _criticalEnd='100' _state='0' nodeType='1054' _showThermometer='0' guiFCC='0' _switchFontSize='13.5' _scalePosition='0' _outChannelName='' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _channelMultiplyExponent='0' _radialScaleBeginingAngle='-90' _tankColor='#000000' _position='-90' _maximum='100' _decimalPlaces='2' _showNeedle='0' _valueTextSize='8' _onColor='#000000' _showValues='1' _buttonColor='#595959' _showSlider='0' _value='0' _textRaidus='67' _offColor='#000000' _scaleLeft='0' _showDigitmeter='1' _genType='1' _startCriticalArea='75' _needleColor='#ed1c24' _genMin='-100' _criticalStart='85' _showIndicator='0' _stepHeight='2' _tagName='' _titleColor='#a0a0a4' _showTitle='0' _genRate='100' guiToolTip='' tooltip='' _blinking='0' _scaleTop='0' _valueStep='20' _lineWidth='4' _mainStepWidth='2' _cautionColor='#808000' _scaleHeight='58' _stepWidth='1' _mainStepFrequency='20' _width='170' _textColor='#ffffff' _scaleType='2' _needleType='2' _positionsNumber='1' guiBCC='0' _stepFrequency='5' _noUnitLable='1' _refreshInterval='50' _startValue='0' _variableName='' _scaleWidth='170' _switchColor='#000000' guiEnabled='1' _valueColor='#ffffff' _endValue='100' _blinkingColor='#000000' _digitmeterColor='#ffffff' _showTank='0' _showTankBackground='1'/></Widget>")
        self.analog_edge1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings _startCautionArea='50' x='160' _unit='' _buttonImageIndex='0' _liquidColor='#d40000' _blinkingTime='50' _textSize='8' _channelId='-1' _typeIndex='0' _thermometerColor='#282828' _needleWidth='3' _channelMultiply='1' _needleHeight='59.5' guiCursor='arrow' height='90' _showSwitch='0' _genConst='0' _showCritical='1' _showCautionArea='1' _radialScaleEndAngle='45' _channelOffsetExponent='0' _height='90' _radialScaleRadius='59.5' _measureScaleType='0' _genMax='100' _scaleDistance='0' _switchAutoFontSize='1' _frameColor='#282828' _mode='12' _titleBackgroundColor='#000000' guiFontColor='#c0c0c0' _frameImageIndex='0' _switchType='0' _digitmeterFont='Virtument-LCD1,35,-1,5,50,0,0,0,0,0' _showScale='1' _takeUnitFromChannel='0' _scaleRadiusRatio='0' y='350' _thickness='2' _showCriticalArea='1' _backgroundColor='#282828' _criticalColor='#ff0000' _showFrame='1' _mainStepHeight='5' guiBackColor='#414141' _titleBackgroundTransparent='1' _channelOffset='0' _titleFont='Arial,18,-1,5,50,0,0,0,0,0' _title='Title' _needleIndex='0' m_editable='0' _valueEndPosition='0' _buttonSize='9' variableName='analog_edge1' _showMeasureScale='0' _showGenerator='0' _scaleColor='#ffffff' guiFC='0' _showBackground='1' _lineStep='5' width='180' _minimum='0' _noOutChannel='0' visible='1' _wholeDigits='3' _radius='0' eventFunctionName='' _name='' _valueStartPosition='135' _criticalEnd='100' _state='0' nodeType='1054' _showThermometer='0' guiFCC='0' _switchFontSize='13.5' _scalePosition='1' _outChannelName='' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' _channelMultiplyExponent='0' _radialScaleBeginingAngle='-45' _tankColor='#000000' _position='-45' _maximum='100' _decimalPlaces='0' _showNeedle='1' _valueTextSize='8' _onColor='#000000' _showValues='1' _buttonColor='#595959' _showSlider='0' _value='0' _textRaidus='59.5' _offColor='#000000' _scaleLeft='0' _showDigitmeter='0' _genType='1' _startCriticalArea='75' _needleColor='#ed1c24' _genMin='-100' _criticalStart='85' _showIndicator='0' _stepHeight='2' _tagName='' _titleColor='#a0a0a4' _showTitle='0' _genRate='100' guiToolTip='' tooltip='' _blinking='0' _scaleTop='0' _valueStep='20' _lineWidth='4' _mainStepWidth='2' _cautionColor='#808000' _scaleHeight='255' _stepWidth='1' _mainStepFrequency='20' _width='180' _textColor='#ffffff' _scaleType='2' _needleType='2' _positionsNumber='1' guiBCC='0' _stepFrequency='5' _noUnitLable='1' _refreshInterval='50' _startValue='0' _variableName='' _scaleWidth='200' _switchColor='#000000' guiEnabled='1' _valueColor='#ffffff' _endValue='100' _blinkingColor='#000000' _digitmeterColor='#ffffff' _showTank='0' _showTankBackground='1'/></Widget>")
        self.button1 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings width='90' eventFunctionName='on_previous' guiBCC='0' nodeType='581' x='50' guiEnabled='1' guiBackColor='#414141' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' guiFC='0' guiFontColor='#c0c0c0' guiToolTip='' guiFCC='0' y='380' variableName='button1' visible='1' text='Previous' guiCursor='arrow' height='22'/></Widget>")
        on_event(self.button1, self.on_previous)
        self.button2 = widget_from_settings(self.w1, "<!DOCTYPE Widget><Widget><GuiSettings width='90' eventFunctionName='on_next' guiBCC='0' nodeType='581' x='360' guiEnabled='1' guiBackColor='#414141' guiFont='MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0' guiFC='0' guiFontColor='#c0c0c0' guiToolTip='' guiFCC='0' y='380' variableName='button2' visible='1' text='Next' guiCursor='arrow' height='22'/></Widget>")
        on_event(self.button2, self.on_next)
        set_widget_layout(self.w1, "")


    

        
    def on_next(self):      

        set_widget_value(self.label2,self.records[self.counter][0])
        set_widget_value(self.analog_edge1,self.records[self.counter][1])
        set_widget_value(self.indicator1,self.records[self.counter][2])
        set_widget_value(self.digitmeter1,self.records[self.counter][1])

        self.counter += 1
        # Close connection
        # conn.close()

    def on_previous(self):
        print('on_previous')
        
        


if __name__ == '__main__':
    a = Interface(0)
    show(a.w1)
    gui_loop()
    
    
