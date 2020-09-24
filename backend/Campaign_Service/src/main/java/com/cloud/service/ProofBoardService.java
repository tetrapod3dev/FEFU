package com.cloud.service;

import java.util.List;

import com.cloud.domain.ProofBoardDto;

public interface ProofBoardService {

	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum);
	public int totalCount(int no, boolean flag);
	public int insertProof(ProofBoardDto dto);
	public int updateProof(int no);
}
