function varargout = interpolation(varargin)
% INTERPOLATION MATLAB code for interpolation.fig
%      INTERPOLATION, by itself, creates a new INTERPOLATION or raises the existing
%      singleton*.
%
%      H = INTERPOLATION returns the handle to a new INTERPOLATION or the handle to
%      the existing singleton*.
%
%      INTERPOLATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in INTERPOLATION.M with the given input arguments.
%
%      INTERPOLATION('Property','Value',...) creates a new INTERPOLATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before interpolation_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to interpolation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help interpolation

% Last Modified by GUIDE v2.5 09-Dec-2018 23:56:29

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @interpolation_OpeningFcn, ...
                   'gui_OutputFcn',  @interpolation_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before interpolation is made visible.
function interpolation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to interpolation (see VARARGIN)

% Choose default command line output for interpolation
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
handles.x=[];
handles.y=[];
handles.num=0;
handles.flag=0;
handles.way=1;
guidata(hObject, handles);

% UIWAIT makes interpolation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = interpolation_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
str1=get(handles.edit5,'String');
str2=get(handles.edit4,'String');
str1=str2double(str1);
str2=str2double(str2);
if isnan(str1)||isnan(str2)        
     errordlg('You must entry a number value','Bad Input','modal')
else
handles.x=[handles.x,str1];
handles.y=[handles.y,str2];
handles.num=handles.num+1;
set(handles.text9,'String',num2str(handles.num));
set(handles.edit5,'String','Input new x0');
set(handles.edit5,'Enable','inactive');
set(handles.edit4,'String','Input new y0');
set(handles.edit4,'Enable','inactive');
guidata(hObject, handles);
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

if handles.flag==0
    if handles.num==0
        errordlg('Only one data to input?','Bad Input','modal')
    else
    str1=get(handles.edit5,'String');
    set(handles.edit5,'Enable','inactive');
    str2=get(handles.edit4,'String');
    set(handles.edit4,'Enable','inactive');
    str1=str2double(str1);
    str2=str2double(str2);
    if isnan(str1)||isnan(str2)        
         errordlg('You must entry a number value','Bad Input','modal')
         return
    else
    handles.x=[handles.x,str1];
    handles.y=[handles.y,str2];
    handles.num=handles.num+1;
    set(handles.text9,'String',num2str(handles.num));
    guidata(hObject, handles);
    end
    end
end
if handles.flag==1
    cla(handles.axes1);
end
s=scatter(handles.x,handles.y,'g','filled');
set(handles.axes1,'box','on');
xlabel('x-axis');
ylabel('y-axis');
hold on;
grid on;
min=handles.x(1);
max=handles.x(1);
for i=1:handles.num
    if handles.x(i)>max
        max=handles.x(i);
    end
    if handles.x(i)<min
        min=handles.x(i);
    end
end
xarray=linspace(min,max,500);
yarray=[];
if handles.way==1
    for i=1:1:500
        yi=spline(handles.x,handles.y,xarray(i));
        yarray=[yarray,yi];
    end
end
if handles.way==2
    for i=1:1:500
        yi=interp1(handles.x,handles.y,xarray(i),'pchip');
        yarray=[yarray,yi];
    end
end
if handles.way==3
    for i=1:1:500
        yi=interp1(handles.x,handles.y,xarray(i),'linear');
        yarray=[yarray,yi];
    end
end
if handles.way==4
    for i=1:1:500
        yi=newton(handles.x,handles.y,xarray(i));
        yarray=[yarray,yi];
    end
end
plot(handles.axes1,xarray,yarray); 
handles.flag=1;
guidata(hObject, handles);



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over edit5.
function edit4_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(hObject, 'String', '', 'Enable', 'on');
uicontrol(hObject);


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over edit4.
function edit5_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if strcmp(get(gcf,'SelectionType'),'normal')
    set(hObject, 'String', '', 'Enable', 'on');
    uicontrol(hObject);
end


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over edit2.
function edit2_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(hObject, 'String', '', 'Enable', 'on');
uicontrol(hObject);


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.flag==0
    errordlg('You must input all data first!','Bad Input','modal')
end
str2=get(handles.edit2,'String');
str2=str2double(str2);
if isnan(str2)        
   errordlg('You must entry a number value','Bad Input','modal')
end
if handles.way==1
result=spline(handles.x,handles.y,str2);
end
if handles.way==2
result=interp1(handles.x,handles.y,str2,'pchip');
end
if handles.way==3
result=interp1(handles.x,handles.y,str2,'linear');
end
if handles.way==4
    result=newton(handles.x,handles.y,str2);
end
set(handles.edit6,'String',num2str(result));
% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
cla(handles.axes1);
set(handles.edit5,'String','Input x0 here');
set(handles.edit5,'Enable','inactive');
set(handles.edit4,'String','Input y0 here');
set(handles.edit4,'Enable','inactive');
set(handles.edit2,'String','x0');
set(handles.edit2,'Enable','inactive');
set(handles.text9,'String','0');
set(handles.edit6,'String','f(x0)');
handles.x=[];
handles.y=[];
handles.num=0;
handles.flag=0;
guidata(hObject, handles);


% --- Executes on button press in radiobutton3.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3
handles.way=1;
guidata(hObject, handles);

% --- Executes on button press in radiobutton3.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3
handles.way=2;
guidata(hObject, handles);

function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3
handles.way=3;
guidata(hObject, handles);


% --- Executes on button press in radiobutton4.
function radiobutton4_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton4
handles.way=4;
guidata(hObject, handles);



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
