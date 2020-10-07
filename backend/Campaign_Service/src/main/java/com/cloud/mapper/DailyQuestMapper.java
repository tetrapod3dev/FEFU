package com.cloud.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import com.cloud.domain.DailyQuestDto;

@Mapper
public interface DailyQuestMapper {

	public List<DailyQuestDto> findAll();
	public List<DailyQuestDto> findByCompleteList(String username);
	public int insertComplete(@Param("username") String username, @Param("no") int no);
	public int updateExp(@Param("username") String username);
	
}
