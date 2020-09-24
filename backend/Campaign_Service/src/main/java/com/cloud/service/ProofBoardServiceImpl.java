package com.cloud.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cloud.domain.ProofBoardDto;
import com.cloud.mapper.ProofBoardMapper;

@Service
public class ProofBoardServiceImpl implements ProofBoardService {

	@Autowired
	private ProofBoardMapper proofMapper;

	@Override
	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum) {
		return proofMapper.findAllByProof(no, flag, startIndex, perPageNum);
	}

	@Override
	public int insertProof(ProofBoardDto dto) {
		return proofMapper.insertProof(dto);
	}

	@Override
	public int updateProof(int no) {
		return proofMapper.updateProof(no);
	}

	@Override
	public int totalCount(int no, boolean flag) {
		return proofMapper.totalCount(no, flag);
	}

	@Override
	public double findTodayPassOfficial(int no) {
		int headcount = proofMapper.findHeadcount(no);
		int pass = proofMapper.findTodayPassOfficial(no);

		return getSoloPercent(pass, headcount);
	}

	@Override
	public List<Map<String, Object>> findWeekPassOfficial(int no) {
		int headcount = proofMapper.findHeadcount(no);
		List<Map<String, Object>> list = proofMapper.findWeekPassOfficial(no);
		for(int i=0; i<list.size(); i++) {
			getTotalPercent(null, headcount);
		}

		return list;
	}

	@Override
	public List<Map<String, Object>> findAllPassPersonal(int no) {
		int duration = proofMapper.findDurationPersonal(no);
		List<Map<String, Object>> list = proofMapper.findAllPassPersonal(no);
		for(int i=0; i<list.size(); i++) {
			getTotalPercent(list.get(i), duration);
		}
		return list;
	}

	@Override
	public double findUserPassPersonal(int no, String username) {
		int duration = proofMapper.findDurationPersonal(no);
		int pass = proofMapper.findUserPassPersonal(no, username);
		System.out.println(duration + " " + pass);
		return getSoloPercent(pass, duration);
	}

	private Map<String, Object> getTotalPercent(Map<String, Object> data, int goal) {
		if (data == null) {
			return null;
		}
		for (String key : data.keySet()) {
			if (key.equals("count")) {
				double per = getSoloPercent((long)data.get(key), goal);
				data.replace(key, per);
			}
		}
		return data;
	}

	private double getSoloPercent(long pass, int goal) {
		double res = ((double) pass / (double) goal) * 100.0;
		return Math.round(res * 100.0) / 100.0;
	}
}
