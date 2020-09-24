package com.cloud.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.ProofBoardDto;

@Mapper
public interface ProofBoardMapper {
	
	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum);
	public int totalCount(int no, boolean flag);
	public int insertProof(ProofBoardDto dto);
	public int updateProof(int no);
}
