package com.cloud.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.UserDto;
import com.cloud.service.UserService;

import io.swagger.annotations.ApiOperation;
import springfox.documentation.annotations.ApiIgnore;

@CrossOrigin(origins = "*")
@RestController
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@ApiOperation(value= "해당 유저 정보 보기")
	@GetMapping(value = "/{username}")
	public ResponseEntity<UserDto> getUser(@PathVariable("username") String username){
		UserDto dto = userService.findByUsername(username);
		return new ResponseEntity<UserDto>(dto, HttpStatus.OK);
	}
	
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
	
	@ApiOperation(value= "유저 정보 변경 (nickname, age, gender, profileImage, introduce) 데이터 누락 주의")
	@PatchMapping(value = "/")
	public ResponseEntity<String> modifyUser(@ApiIgnore @RequestHeader("X-USERNAME") String username, @RequestBody UserDto dto){
		dto.setUsername(username);
		int res = userService.updateUser(dto);
		if(res == 0) {
			return new ResponseEntity<String>("변경실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("변경완료", HttpStatus.OK);
	}
	
	@ApiOperation(value= "비밀번호 변경")
	@PatchMapping(value = "/password")
	public ResponseEntity<String> modifyPassword(@ApiIgnore @RequestHeader("X-USERNAME") String username, @RequestBody Map<String, String> map){
		String password = map.get("password");
		int res = userService.changePassword(password, username);
		if(res == 0) {
			return new ResponseEntity<String>("변경실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("변경완료", HttpStatus.OK);
	}
}
