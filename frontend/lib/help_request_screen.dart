import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class HelpRequestScreen extends StatefulWidget {
  @override
  _HelpRequestScreenState createState() => _HelpRequestScreenState();
}

class _HelpRequestScreenState extends State<HelpRequestScreen> {
  final TextEditingController _descriptionController = TextEditingController();
  String _errorMessage = '';
  String _successMessage = '';

  void _submitRequest() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String? token = prefs.getString('token');

    if (token == null) {
      setState(() {
        _errorMessage = 'No token found. Please log in again.';
      });
      return;
    }

    try {
      final response = await http.post(
        Uri.parse('http://localhost:8000/api/help-requests/submit_request/'),
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
        },
        body: json.encode({
          'description': _descriptionController.text,
        }),
      );

      if (response.statusCode == 200) {
        setState(() {
          _successMessage = 'Help request submitted successfully!';
          _errorMessage = '';
          _descriptionController.clear();
        });
      } else {
        setState(() {
          _errorMessage = 'Failed to submit help request. Please try again.';
          _successMessage = '';
        });
      }
    } catch (e) {
      print('Error: $e');
      setState(() {
        _errorMessage = 'An error occurred. Please try again later.';
        _successMessage = '';
      });
    }
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Submit Help Request')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: _descriptionController,
              decoration: InputDecoration(labelText: 'Description'),
            ),
            ElevatedButton(
              onPressed: _submitRequest,
              child: Text('Submit'),
            ),
            if (_successMessage.isNotEmpty)
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  _successMessage,
                  style: TextStyle(color: Colors.green),
                ),
              ),
            if (_errorMessage.isNotEmpty)
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  _errorMessage,
                  style: TextStyle(color: Colors.red),
                ),
              ),
          ],
        ),
      ),
    );
  }
}