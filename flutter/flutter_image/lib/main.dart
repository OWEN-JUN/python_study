import 'package:countdown/countdown.dart';
import 'dart:io';
import 'package:image/image.dart' as im;
import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:async_loader/async_loader.dart';
void main() => runApp(MaterialApp(
    title: "camera app",
    home: LandingScreen()

));


class LandingScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<LandingScreen> {

  bool isLoading = false;

  bool conversion = false;
  File imageFile;
  File conv_img;
  File socket_img;
  Future consocket() async {
    int port = 9009;
    Socket socket = await Socket.connect("192.168.0.158",port);

    socket.add(utf8.encode('1.png'));
    List<int> buffer = [];
    await for (List<int> v in socket.asBroadcastStream()) {
      buffer.addAll(v);
      print(v.length);
      if (v.length == 0) {
        break;
      }
    }

    print("buffer len: "+ buffer.length.toString());

    socket_img = await File("assets/server.jpg").writeAsBytes(buffer);

  }
  Widget _sockimg(){
    if(socket_img == null){
      return Text("no image selected!");

    } else{
      return Image.file(socket_img, width: 400, height: 400,);
    }

  }
  _openGallary(BuildContext context) async{
    var picture = await ImagePicker.pickImage(source: ImageSource.gallery);
    this.setState((){
      imageFile = picture;

    });
    Navigator.of(context).pop();
  }
  _openCamera(BuildContext context) async{
    var picture = await ImagePicker.pickImage(source: ImageSource.camera);
    this.setState((){
      imageFile = picture;

    });
    Navigator.of(context).pop();
  }
  _conversion(BuildContext context) async {
    this.setState(() {
      if (conversion != false){conv_img = imageFile;}
    });
  }


  Future<void> _showChoiceDialog(BuildContext context){
    return showDialog(context: context, builder: (BuildContext context){
      return AlertDialog(
        title: Text("make a choice!"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[
              GestureDetector(
                child: Text("Gallary"),
                onTap: (){
                  _openGallary(context);
                },
              ),
              Padding(padding: EdgeInsets.all(8.0)),
              GestureDetector(
                child: Text("Camera"),
                onTap: (){
                  _openCamera(context);
                },
              )
            ],
          ),
        ),
      );
    });
  }
    Future<void> _showconvimg(BuildContext context){
      _conversion(context);
    }

  Widget _decideImageView(){
    if(imageFile == null){
      return Text("no image selected!");

    } else{
      return Image.file(imageFile, width: 400, height: 400,);
    }

  }
  Widget delay_image(){
    if(conv_img == null){
      return Text("no image!");

    } else{
      return Text("put the conversion button");
      }
    }

  Widget conversion_img(){
    if(conv_img != null ){
      conversion = false;
      return Image.file(imageFile, width: 400, height: 400,);

    } else{
      return Text("put the conversion button");
    }
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("main station")
      ),
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              Padding(padding: EdgeInsets.all(20.0)),
              Container(
                  alignment: Alignment.center,
                  width: 400,
                  height: 400,
//                  child: _decideImageView(),
                  child: _sockimg(),
              ),

              Padding(padding: EdgeInsets.all(10.0)),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  RaisedButton(onPressed: (){
                    consocket();
                  },
                    child: Text("socket"),
                  ),
                  RaisedButton(onPressed: (){
                    _showChoiceDialog(context);
                  },
                    child: Text("Select image"),
                  ),
                  Padding(padding: EdgeInsets.all(5.0)),
                  RaisedButton(onPressed: (){
                    if (imageFile != null) {
                      isLoading = true;
                      _showconvimg(context);
                      Future.delayed(const Duration(seconds: 3), () {
                        isLoading = false;
                        conversion = true;
                        _showconvimg(context);
                      });
                    }
                  },
                    child: Text("Conversion"),
                  ),
                ],
              ),

              Padding(padding: EdgeInsets.all(10.0)),
              Container(
                alignment: Alignment.center,
                width: 400,
                height: 400,
                child: conversion ? Center(
                  child: conversion_img(),

                )
                :isLoading ? Center(
                  child: CircularProgressIndicator()
                )
                :delay_image(),

              ),
              Padding(padding: EdgeInsets.all(10.0)),

            ],
          ),
        ),
      ),
    );
  }

}

