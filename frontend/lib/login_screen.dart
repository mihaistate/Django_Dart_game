import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  String _errorMessage = '';

void _login() async {
  try {
    final response = await http.post(
      Uri.parse('http://localhost:8000/api/token/'),
      body: {
        'username': _emailController.text,
        'password': _passwordController.text,
      },
    );


      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        print('Response data: $data');  // Debugging line

        if (data.containsKey('access')) {  // Check for the correct key
          final token = data['access'];  // Use 'access' instead of 'token'

          // Save token using SharedPreferences
          SharedPreferences prefs = await SharedPreferences.getInstance();
          await prefs.setString('token', token);

          // Navigate to the next screen
          Navigator.pushNamed(context, '/help');
        } else {
          setState(() {
            _errorMessage = 'Login failed. Token not found.';
          });
        }
      } else {
        setState(() {
          _errorMessage = 'Login failed. Please check your email and password.';
        });
      }
    } catch (e) {
      print('Error: $e');  // Debugging line
      setState(() {
        _errorMessage = 'An error occurred. Please try again later.';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: _emailController,
              decoration: InputDecoration(labelText: 'Email'),
            ),
            TextField(
              controller: _passwordController,
              decoration: InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            ElevatedButton(
              onPressed: _login,
              child: Text('Login'),
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