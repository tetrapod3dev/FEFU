package com.cloud.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.UserDto;
import com.cloud.service.UserService;

@RestController
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@PostMapping(value = "/")
	public ResponseEntity<String> signup(@RequestBody UserDto dto){
		int res = userService.userRegistier(dto);
		if(res == 0) {
			return new ResponseEntity<String>("FAIL", HttpStatus.OK);
		}
		return new ResponseEntity<String>("OK", HttpStatus.OK);
	}
	
	@GetMapping(value = "/check-email/{email}")
	public ResponseEntity<String> checkEmail(@PathVariable("email") String username){
		int res = userService.checkByUsername(username);
		if(res == 0) {
			return new ResponseEntity<String>("OK", HttpStatus.OK);
		}
		return new ResponseEntity<String>("FAIL", HttpStatus.OK);
	}
}
