package com.cloud.service;

import com.cloud.domain.UserDto;

public interface UserService {
	
	public UserDto findByUsername(String username);
	public int userRegistier(UserDto dto);
	public int updateUser(UserDto dto);
	public int changePassword(String password, String username);
	public int checkByUsername(String usernmae);
	public int checkByNickname(String nickname);
	public int insertUserRole(String usernmae);
	public int updateEco(String sender, String receiver, int point);
}
