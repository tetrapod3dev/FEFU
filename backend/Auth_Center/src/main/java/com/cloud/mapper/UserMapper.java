package com.cloud.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.UserDto;

@Mapper
public interface UserMapper {
	public UserDto findByUsername(String username);
	public List<String> findAuthority(String username);
}
