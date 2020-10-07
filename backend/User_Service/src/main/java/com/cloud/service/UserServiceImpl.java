package com.cloud.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cloud.domain.EcoPointDto;
import com.cloud.domain.UserDto;
import com.cloud.mapper.UserMapper;

@Service
public class UserServiceImpl implements UserService{

	@Autowired
	private UserMapper userMapper;
	
	@Autowired
	private PasswordEncoder passwordEncoder;
	
	@Override
	@Transactional
	public int userRegistier(UserDto dto) {
		dto.setPassword(passwordEncoder.encode(dto.getPassword()));
		int res = userMapper.userRegistier(dto);
		if(res != 0) {
			userMapper.insertUserRole(dto.getUsername());
		}
		return res;
	}
	
	@Override
	public List<EcoPointDto> findByEcoPointList(String username) {
		return userMapper.findByEcoPointList(username);
	}
	
	@Override
	public int changePassword(String password, String username) {
		password = passwordEncoder.encode(password);
		return userMapper.changePassword(password, username);
	}
	
	@Override
	public int updateEco(String sender, String receiver, int point) {
		return userMapper.updateEco(sender, receiver, point);
	}
	
	@Override
	public int updateUser(UserDto dto) {
		return userMapper.updateUser(dto);
	}

	@Override
	public int checkByUsername(String usernmae) {
		return userMapper.checkByUsername(usernmae);
	}
	
	@Override
	public int checkByNickname(String nickname) {
		return userMapper.checkByNickname(nickname);
	}
	
	@Override
	public int insertUserRole(String usernmae) {
		return userMapper.insertUserRole(usernmae);
	}
	
	@Override
	public UserDto findByUsername(String username) {
		return userMapper.findByUsername(username);
	}

}
