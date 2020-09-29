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

import io.swagger.annotations.ApiOperation;

@RestController
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@ApiOperation(value= "회원가입")
	@PostMapping(value = "/")
	public ResponseEntity<String> signup(@RequestBody UserDto dto){
		int res = userService.userRegistier(dto);
		if(res == 0) {
			return new ResponseEntity<String>("등록실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("등록성공", HttpStatus.OK);
	}
	
	@ApiOperation(value= "이메일 중복 체크")
	@GetMapping(value = "/check-email/{email}")
	public ResponseEntity<String> checkEmail(@PathVariable("email") String username){
		int res = userService.checkByUsername(username);
		if(res == 0) {
			return new ResponseEntity<String>("사용가능", HttpStatus.OK);
		}
		return new ResponseEntity<String>("사용불가능", HttpStatus.OK);
	}
	
	@ApiOperation(value= "닉네임 중복 체크")
	@GetMapping(value = "/check-nickname/{nickname}")
	public ResponseEntity<String> checkNickname(@PathVariable("nickname") String nickname){
		int res = userService.checkByNickname(nickname);
		if(res == 0) {
			return new ResponseEntity<String>("사용가능", HttpStatus.OK);
		}
		return new ResponseEntity<String>("사용불가능", HttpStatus.OK);
	}
}
