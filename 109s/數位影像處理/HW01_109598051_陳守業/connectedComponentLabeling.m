function[] = connectedComponentLabeling(adjacency, fileName) % adjacency = 4/8
    
	inputArray = csvread(fileName)
	
	outputArray = inputArray;
	newAreaNumber = 1;

    arraySize = size(outputArray);
    height = arraySize(1);
    width = arraySize(2);
    
    for i = 1 : height
        for j = 1 : width
	   
            if inputArray(i, j) == 1
				
				% get neighbor(s) & its/their label(s)...
				neighbor = []; % existing neighbor(s)
				nonZeroLabel = []; % existing neighbor(s) --> non-zero label(s)
				
				up = -1;
				left = -1;
				if i > 1
					up = inputArray(i-1, j);
					neighbor = [neighbor, up];
					if up == 1
						nonZeroLabel = [nonZeroLabel, outputArray(i-1, j)];
					end
				end
				if j > 1
					left = inputArray(i, j-1);
					neighbor = [neighbor, left];
					if left == 1
						nonZeroLabel = [nonZeroLabel, outputArray(i, j-1)];
					end
				end
				
				if adjacency == 8 % 8-adjacency needed only
					upLeft = -1;
					upRight = -1;
					if i > 1
						if j > 1
							upLeft = inputArray(i-1, j-1);
							neighbor = [neighbor, upLeft];
							if upLeft == 1
								nonZeroLabel = [nonZeroLabel, outputArray(i-1, j-1)];
							end
						end
						if j < length(inputArray(i-1, :))
							upRight = inputArray(i-1, j+1);
							neighbor = [neighbor, upRight];
							if upRight == 1
								nonZeroLabel = [nonZeroLabel, outputArray(i-1, j+1)];
							end
						end
					end
					
				end
				% ...get neighbor(s) & its/their label(s)
				
				% update label(s)...
				if neighbor == zeros(length(neighbor)) % no non-zero label neighbor --> assign new label--'newAreaNumber'
					outputArray(i, j) = newAreaNumber;
					newAreaNumber = newAreaNumber + 1;
                elseif isempty(neighbor) % no neighbor(return value of '==' op. may make '||' op. unable to work, so put it here) --> assign new label--'newAreaNumber'
                    outputArray(i, j) = newAreaNumber;
					newAreaNumber = newAreaNumber + 1;
                elseif ~isempty(nonZeroLabel) % non-zero label neighbor exists --> adjust label(s)
					
					% current element, non-zero label neighbor(s) --> minimum label among non-zero label neighbor(s)--'minLabel'
					minLabel = min(nonZeroLabel);
					outputArray(i, j) = minLabel;
                    if up == 1
						outputArray(i-1, j) = minLabel;
                    end
                    if left == 1
						outputArray(i, j-1) = minLabel;
                    end
                    if adjacency == 8
                        if upLeft == 1
							outputArray(i-1, j-1) = minLabel;
                        end
                        if upRight == 1
							outputArray(i-1, j+1) = minLabel;
                        end
                    end
					
					% change all passed label(s) in the same region to 'minLabel'
					for k = nonZeroLabel
						if k > minLabel
							s = 1;
							t = 1;
							while s ~= i || t ~= j
                                if outputArray(s, t) == k
									outputArray(s, t) = minLabel;
                                end
                                if s == height
									break
                                end
								if t == width
									t = 1;
                                    s = s + 1;
                                else
                                    t = t + 1;
								end
							end
						end
					end
				end
				% ...update label(s)
				
            end
        end
    end
	
	outputArray
	
return
 
